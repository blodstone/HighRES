import random
import string
from datetime import datetime

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.sql.expression import func

from backend.model.project import FluencyProject
from backend.model.result import FluencyResultSchema, FluencyResult
from backend.model.project_status import ProjectStatus, ProjectStatusSchema
from backend.model import ma, db
from backend.model.summary import SummarySchema, SanitySummarySchema, Summary, SanitySummary


class ResSumObj(object):
    def __init__(self, result, summary):
        self.result = result
        self.summary = summary


class ResSumSchema(ma.Schema):
    result = ma.Nested(FluencyResultSchema)
    summary = ma.Nested(SummarySchema)


class FluencyObj(object):
    def __init__(self, res_sums, sanity_summ, proj_status):
        self.res_sums = res_sums
        self.sanity_summ = sanity_summ
        self.proj_status = proj_status


class FluencySchema(ma.Schema):
    res_sums = ma.Nested(ResSumSchema, many=True)
    sanity_summ = ma.Nested(SanitySummarySchema)
    proj_status = ma.Nested(ProjectStatusSchema)


class FluencyResource(Resource):

    def post(self, project_id):
        results = request.get_json()
        for result in results:
            result_query = FluencyResult.query.get(result['id'])
            result_query.fluency = result['fluency']
            result_query.clarity = result['clarity']
            db.session.commit()

    def get(self, project_id):
        project = FluencyProject.query.get(project_id)
        if project is None:
            return abort(404, message=f"Fluency project {project_id} not found")
        else:
            # Get one unfinished project_status
            proj_status = ProjectStatus.query\
                .filter_by(fluency_proj_id=project.id, is_finished=False, is_active=False)\
                .order_by(func.rand())\
                .first()

            # Get related results
            results = FluencyResult.query\
                .filter_by(proj_status_id=proj_status.id, is_invalid=False)\
                .all()

            res_sums = []
            for result in results:
                summary = Summary.query.get(result.summary_id)
                res_sums.append(ResSumObj(result=result, summary=summary))

            # Get random sanity summaries
            # The function rand() is specific to MySql only (https://stackoverflow.com/q/60805)
            sanity_summ = SanitySummary.query.order_by(func.rand()).first()
            fluency = FluencyObj(
                res_sums=res_sums,
                sanity_summ=sanity_summ,
                proj_status=proj_status)
            return FluencySchema().dump(fluency)


