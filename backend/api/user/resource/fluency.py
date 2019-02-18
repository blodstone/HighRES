import random
import string

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.sql.expression import func

from backend.model.project import EvaluationProject
from backend.model.result import FluencyResultSchema, FluencyResult
from backend.model.project_status import ProjectStatus
from backend.model import ma, db
from backend.model.summary import SummarySchema, SanitySummarySchema, Summary, SanitySummary


class FluencyObj(object):
    def __init__(self, results, summaries, sanity_summ, mturk_code):
        self.results = results
        self.summaries = summaries
        self.sanity_summ = sanity_summ
        self.mturk_code = mturk_code


class FluencySchema(ma.Schema):
    class Meta:
        fields = ('results', 'summaries', 'sanity_summ', 'mturk_code')
    results = ma.Nested(FluencyResultSchema, many=True)
    summaries = ma.Nested(SummarySchema, many=True)
    sanity_summ = ma.Nested(SanitySummarySchema)


class FluencyResource(Resource):

    def post(self, project_id):
        results = request.get_json()
        for result in results:
            result_query = FluencyResult.query.get(result['id'])
            result_query.fluency = result['fluency']
            result_query.clarity = result['clarity']
            db.session.commit()

    def get(self, project_id):
        n = request.args.get('n')
        project = EvaluationProject.query.get(project_id)
        if not project:
            return abort(404, message=f"Project {project_id} not found")
        else:

            # Get unfinished project_status
            proj_statuses = ProjectStatus.query\
                .filter_by(eval_proj_id=project.id, is_finished=False)\
                .order_by(func.rand())\
                .limit(n).all()

            # Get related summaries
            summary_ids = [p.summary_id for p in proj_statuses]
            summaries = Summary.query.filter(Summary.id.in_(summary_ids)).all()

            # Create n results
            results = []
            randomwords = lambda n: ''.join(
                random.choice(string.ascii_lowercase) for _ in range(n))
            mturk_code = f"{randomwords(8)}_{project.id}"
            for p in proj_statuses:
                result = FluencyResult(
                    mturk_code=mturk_code,
                    proj_status_id=p.id
                )
                db.session.add(result)
                db.session.commit()
                results.append(result)

            # Get random sanity summaries
            # The function rand() is specific to MySql only (https://stackoverflow.com/q/60805)
            sanity_summ = SanitySummary.query.order_by(func.rand()).first()
            fluency = FluencyObj(results=results, summaries=summaries, sanity_summ=sanity_summ, mturk_code=mturk_code)
            return FluencySchema().dump(fluency)


