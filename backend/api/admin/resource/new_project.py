import string
from random import shuffle, random, choice

from flask import request
from flask_restful import Resource, abort

from backend.model.dataset import Dataset, DatasetSchema
from backend.model.project import ProjectType, FluencyProject
from backend.model.project_status import ProjectStatus
from backend.model.result import FluencyResult
from backend.model.summary import SummaryGroupList, SummaryGroup
from backend.model import db, ma


class DatasetsResource(Resource):
    """
    Resource for dataset selection
    """
    def get(self):
        result = Dataset.query.all()
        schema = DatasetSchema(many=True, only=('id', 'name', 'summ_groups'))
        if len(result) > 0:
            return schema.dump(result)
        else:
            abort(404, message='Empty datasets or summary groups!')


class ProjectResource(Resource):
    """
    Resource for project
    """
    def put(self, type):
        project = request.get_json()
        if type.lower() == ProjectType.EVALUATION.value.lower():
            proj_id = self.create_project(project)
            self.create_project_result(project, proj_id)

    def create_project(self, project):
        # noinspection PyArgumentList
        new_project = FluencyProject(
            name=project['name'],
            category=project['category'])
        db.session.add(new_project)
        db.session.commit()
        for summ_group in project['summ_group_list']:
            new_summ_group_list = SummaryGroupList(
                summ_group_id=summ_group['id'],
                proj_id=new_project.id
            )
            db.session.add(new_summ_group_list)
            db.session.commit()
        return new_project.id

    # def create_project_status(self, project, proj_id):
    #     for system_summary_id in project['summ_group']['summaries']:
    #         new_summ_status = ProjectStatus(
    #             summary_id=system_summary_id,
    #             eval_proj_id=proj_id,
    #             total_exp_results=project['total_exp_results'],
    #         )
    #         db.session.add(new_summ_status)
    #         db.session.commit()

    def create_project_result(self, project, proj_id):
        summ_groups = SummaryGroup.query\
            .join(SummaryGroupList)\
            .join(FluencyProject)\
            .filter_by(id=proj_id).all()
        # Create results
        results = []
        for summ_group in summ_groups:
            for summary in summ_group.summaries:
                results.append(FluencyResult(summary_id=summary.id, proj_status_id=0))
        shuffle(results)

        def chunks(l, n):
            """Yield successive n-sized chunks from l."""
            for i in range(0, len(l), n):
                yield l[i:i + n]

        # Create proj status
        result_chunks = list(chunks(results, project['n_summaries']))
        for chunk in result_chunks:
            # Pre-generated all the random mturk_code
            randomwords = lambda n: ''.join(
                choice(string.ascii_lowercase) for _ in range(n))
            mturk_code = f"{randomwords(8)}_{proj_id}"

            # For each chunk assign a project status
            new_proj_status = ProjectStatus(
                mturk_code=mturk_code,
                fluency_proj_id=proj_id,
            )
            db.session.add(new_proj_status)
            db.session.commit()

            for result in chunk:
                result.proj_status_id = new_proj_status.id
            db.session.bulk_save_objects(chunk)
            db.session.commit()



