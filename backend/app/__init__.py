"""
Initialize Flask application.
"""
import os
import json

from flask import Flask, render_template, make_response
from flask_debugtoolbar import DebugToolbarExtension

from backend.api.admin import admin_api
from backend.api.user import user_api
from backend.model import db, ma
from backend.model.dataset import Dataset
from backend.model.document import Document
from backend.model.summary import Summary, SummaryGroup, SanitySummary


class CustomFlask(Flask):
    """
    Custom Flask application to override the Jinja's tag
    to avoid conflict with Vue's tag
    """
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='<%',
        block_end_string='%>',
        variable_start_string='%%',
        variable_end_string='%%',
        comment_start_string='<#',
        comment_end_string='#>',
    ))


def create_app(config, is_testing):
    """
    Create the app for flask run
    """
    app = CustomFlask(__name__, instance_relative_config=True,
                      static_folder='../../instance/dist/static',
                      template_folder='../../instance/dist')
    app.register_blueprint(admin_api, url_prefix='/admin')
    app.register_blueprint(user_api)
    if is_testing:
        app.config['TESTING'] = config.TESTING
        db_uri = config.SQLALCHEMY_DATABASE_URI
        is_init_db = config.IS_INIT_DB
        dataset_path = config.DATASET_PATH
    else:
        db_uri = os.getenv('DB_URI')
        is_init_db = os.getenv('IS_INIT_DB')
        dataset_path = os.getenv('DATASET_PATH')
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=db_uri,
        SQLALCHEMY_TRACK_MODIFICATIONS=True,
        DEBUG_TB_PROFILER_ENABLED=True
    )
    db.init_app(app)
    ma.init_app(app)

    @app.route('/')
    def index():
        """
        Render the vue generated html
        """
        return render_template('index.html')

    @app.route('/app.js')
    def send_app_js():
        headers = {"Content-Disposition": "attachment; filename=%s" % 'app.js'}
        path = os.path.join(app.instance_path, 'dist', 'app.js')
        with open(path, 'r') as f:
            body = f.read()
        return make_response((body, headers))

    if is_init_db:
        with app.app_context():
            init_db(dataset_path, db)

    toolbar = DebugToolbarExtension(app)
    return app


def init_db(dataset_path, db):
    db.drop_all()
    db.create_all()
    dataset_name = os.path.split(dataset_path)[1]
    summaries_path = os.path.join(dataset_path, 'summaries')
    documents_path = os.path.join(dataset_path, 'documents')
    sanity_path = os.path.join(dataset_path, 'sanity')
    sanity_2_path = os.path.join(dataset_path, 'sanity_2')
    sanity_summ_path = os.path.join(dataset_path, 'sanity_summary')

    # Insert dataset
    dataset = Dataset(name=dataset_name)
    db.session.add(dataset)
    db.session.commit()

    # Insert documents
    for file in os.listdir(documents_path):
        file_path = os.path.join(documents_path, file)
        sanity_file_path = os.path.join(sanity_path, f"{file.split('.')[0]}.json")
        sanity_file_2_path = os.path.join(sanity_2_path, f"{file.split('.')[0]}.json")
        with open(file_path, 'r') as infile:
            sanity = open(sanity_file_path, 'r')
            sanity_2 = open(sanity_file_2_path, 'r')
            json_result = json.load(infile)
            sanity_json = json.load(sanity)
            sanity_2_json = json.load(sanity_2)
            document = Document(
                dataset_id=dataset.id,
                doc_id=json_result['doc_id'],
                doc_json=json_result,
                sanity_statement=sanity_json['statement'],
                sanity_answer=sanity_json['answer'],
                sanity_statement_2=sanity_2_json['statement'],
                sanity_answer_2=sanity_2_json['answer'],
            )
            db.session.add(document)
            db.session.commit()
            sanity.close()
            sanity_2.close()

    # Insert Summaries
    for folder in os.listdir(summaries_path):
        if folder.startswith('ref'):
            summary_group = SummaryGroup(name='%s_ref_%s' % (dataset_name, folder[4:]),
                                         dataset_id=dataset.id, is_ref=True)
        elif folder.startswith('system'):
            summary_group = SummaryGroup(name='%s_system_%s' % (dataset_name, folder[7:]),
                                         dataset_id=dataset.id, is_ref=False)
        else:
            break
        db.session.add(summary_group)
        db.session.commit()
        ref_path = os.path.join(summaries_path, folder)
        for file in os.listdir(ref_path):
            with open(os.path.join(ref_path, file), 'r') as infile:
                text = ' '.join(infile.readlines()).strip()
                document = db.session.query(Document).filter_by(doc_id=os.path.splitext(file)[0]).first()
                summary = Summary(
                    doc_id=document.id,
                    text=text,
                    summary_group_id=summary_group.id
                )
                db.session.add(summary)
                db.session.commit()

    # Insert sanity summaries
    for file in os.listdir(sanity_summ_path):
        file_path = os.path.join(sanity_summ_path, file)
        with open(file_path, 'r') as infile:
            json_infile = json.load(infile)
            sanity_summary = SanitySummary(
                best_summary=json_infile['best'].lower(),
                avg_summary=json_infile['average'].lower(),
                worst_summary=json_infile['worst'].lower(),
                dataset_id=dataset.id
            )
            db.session.add(sanity_summary)
            db.session.commit()


