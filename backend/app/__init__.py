"""
Initialize Flask application.
"""
import os

from flask import Flask, render_template, make_response

from backend.api.admin import admin_api
from backend.api.user import user_api
from backend.model import db, ma


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
    else:
        db_uri = os.getenv('db_uri')
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=db_uri,
        SQLALCHEMY_TRACK_MODIFICATIONS=True,
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

    return app
