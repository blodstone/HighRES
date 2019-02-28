from datetime import datetime, timedelta
from random import shuffle

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.sql.expression import func

from backend.model.project import ClarityProject
from backend.model.result import ClarityResultSchema, ClarityResult
from backend.model.project_status import ProjectStatus, ProjectStatusSchema
from backend.model import ma, db
from backend.model.summary import SummarySchema, SanitySummarySchema, \
    Summary, SanitySummary


class ResSumObj(object):
    def __init__(self, result, summary):
        self.result = result
        self.summary = summary


class ResSumSchema(ma.Schema):
    result = ma.Nested(ClarityResultSchema)
    summary = ma.Nested(SummarySchema)


class ClarityObj(object):
    def __init__(self, res_sums, sanity_summ, proj_status):
        self.res_sums = res_sums
        self.sanity_summ = sanity_summ
        self.proj_status = proj_status


class ClaritySchema(ma.Schema):
    res_sums = ma.Nested(ResSumSchema, many=True)
    sanity_summ = ma.Nested(SanitySummarySchema)
    proj_status = ma.Nested(ProjectStatusSchema)


class ClarityResource(Resource):

    def post(self):
        data = request.get_json()
        old_results = []
        # print(data['results'])
        for result in data['results']:
            old_result = ClarityResult.query.get(result['id'])
            old_result.clarity = result['clarity']
            old_results.append(old_result)
        proj_status = ProjectStatus.query.get(data['proj_status']['id'])
        proj_status.validity = data['proj_status']['validity']
        proj_status.is_finished = data['proj_status']['is_finished']
        proj_status.is_active = data['proj_status']['is_active']
        proj_status.good_summ_score = data['proj_status']['good_summ_score']
        proj_status.mediocre_summ_score = data['proj_status']['mediocre_summ_score']
        proj_status.bad_summ_score = data['proj_status']['bad_summ_score']
        proj_status.sanity_summ_id = data['proj_status']['sanity_summ_id']
        if not proj_status.validity:
            # Recreate results
            results = []
            for result in data['results']:
                new_result = ClarityResult(
                    summary_id=result['summary_id'],
                    proj_status_id=result['proj_status_id'])
                results.append(new_result)
            db.session.bulk_save_objects(results)
            # Invalidate old results
            for old_result in old_results:
                old_result.is_invalid = True
        db.session.commit()

    def get(self, project_id):
        project = ClarityProject.query.get(project_id)
        if project is None:
            return abort(404, message=f"Clarity project {project_id} not found")
        else:
            # Get one unfinished project_status
            current_time = datetime.utcnow()
            proj_status = ProjectStatus.query\
                .filter_by(clarity_proj_id=project.id,
                           is_finished=False, is_active=False)\
                .order_by(func.rand())\
                .first()
            if proj_status is None:
                proj_status = ProjectStatus.query \
                    .filter_by(clarity_proj_id=project.id, is_finished=False)\
                    .filter(ProjectStatus.expired_in < current_time)\
                    .order_by(func.rand())\
                    .first()
            if proj_status is None:
                return abort(404, message=f"No project status is opened.")
            # Get related results
            results = ClarityResult.query\
                .filter_by(proj_status_id=proj_status.id, is_invalid=False)\
                .all()

            res_sums = []
            for result in results:
                summary = Summary.query.get(result.summary_id)
                res_sums.append(ResSumObj(result=result, summary=summary))

            # Get random sanity summaries
            # The function rand() is specific to MySql only (https://stackoverflow.com/q/60805)
            sanity_summ = SanitySummary.query.order_by(func.rand()).first()
            clarity = ClarityObj(
                res_sums=res_sums,
                sanity_summ=sanity_summ,
                proj_status=proj_status)

            # Change project status attribute before sending
            proj_status.is_active = True
            proj_status.expired_in = datetime.utcnow() + timedelta(minutes=project.expire_duration)
            db.session.commit()
            return ClaritySchema().dump(clarity)


