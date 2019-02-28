import string
from random import shuffle, choice

from flask import request
from flask_restful import Resource, abort

from backend.model.dataset import Dataset, DatasetSchema
from backend.model.project import ClarityProject
from backend.model.project_status import ProjectStatus
from backend.model.result import ClarityResult
from backend.model.summary import SummaryGroupList, SummaryGroup
from backend.model import db


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


class ClarityResource(Resource):
    """
    Resource for project
    """
    def put(self):
        project_json = request.get_json()
        project = self.__create_project(project_json)
        self.__create_project_result(project)

    def delete(self, project_id):
        project = ClarityProject.query.get(project_id)
        if project:
            db.session.delete(project)
            db.session.commit()
        else:
            abort(404, message=f"Project {project_id} not found")

    def __create_project(self, project_json):
        # noinspection PyArgumentList
        new_project = ClarityProject(
            name=project_json['name'],
            category=project_json['category'],
            expire_duration=project_json['expire_duration'],
            total_exp_results=project_json['total_exp_results']
        )
        db.session.add(new_project)
        db.session.commit()
        summ_group_lists = []
        for summ_group in project_json['summ_group_list']:
            new_summ_group_list = SummaryGroupList(
                summ_group_id=summ_group['id'],
                clarity_proj_id=new_project.id
            )
            summ_group_lists.append(new_summ_group_list)
        db.session.bulk_save_objects(summ_group_lists)
        db.session.commit()
        return new_project

    def __create_project_result(self, project):
        summ_groups = SummaryGroup.query\
            .join(SummaryGroupList)\
            .join(ClarityProject)\
            .filter_by(id=project.id).all()

        for i in range(project.total_exp_results):
            # Create results
            results = []
            for summ_group in summ_groups:
                for summary in summ_group.summaries:
                    results.append(ClarityResult(
                        summary_id=summary.id, proj_status_id=0))
            shuffle(results)

            def chunks(l, n):
                """Yield successive n-sized chunks from l."""
                for i in range(0, len(l), n):
                    yield l[i:i + n]

            # Create proj status
            result_chunks = list(chunks(results, project.n_summaries))
            for chunk in result_chunks:
                # Pre-generated all the random mturk_code
                randomwords = lambda n: ''.join(
                    choice(string.ascii_lowercase) for _ in range(n))
                mturk_code = f"{randomwords(8)}_{project.id}"

                # For each chunk assign a project status
                new_proj_status = ProjectStatus(
                    mturk_code=mturk_code,
                    clarity_proj_id=project.id,
                )
                db.session.add(new_proj_status)
                db.session.commit()
                # Every results in the chunk is created in the database
                for result in chunk:
                    result.proj_status_id = new_proj_status.id
                db.session.bulk_save_objects(chunk)
                db.session.commit()


