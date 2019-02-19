import string
from random import shuffle, choice
from datetime import datetime, timedelta

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


class FluencyResource(Resource):
    """
    Resource for project
    """
    def put(self):
        project = request.get_json()
        proj_id = self.__create_project(project)
        self.__create_project_result(project, proj_id)

    def delete(self, project_id):
        project = FluencyProject.query.get(project_id)
        if project:
            db.session.delete(project)
            db.session.commit()
        else:
            abort(404, message=f"Project {project_id} not found")

    def __create_project(self, project):
        # noinspection PyArgumentList
        new_project = FluencyProject(
            name=project['name'],
            category=project['category'],
            expire_duration=project['expire_duration']
        )
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

    def __create_project_result(self, project, proj_id):
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

            # Every results in the chunk is created in the database
            for result in chunk:
                result.proj_status_id = new_proj_status.id
            db.session.bulk_save_objects(chunk)
            db.session.commit()


