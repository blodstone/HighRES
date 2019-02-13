import json

from flask import request
from flask_restful import Resource, abort

from backend.model.dataset import Dataset, DatasetSchema
from backend.model.project import ProjectType
from backend.model.summary import SummaryGroupSchema
from backend.model.project import EvaluationProject
from backend.model.project_status import ProjectStatus
from backend.model import db, ma


class ProjectSchema(ma.ModelSchema):
    class Meta:
        model = EvaluationProject


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
            self.create_project_status(project, proj_id)

    def create_project(self, project):
        # noinspection PyArgumentList
        new_project = EvaluationProject(
            name=project['name'],
            category=project['category'],
            summ_group_id=project['summ_group']['id'],
            highlight=False)
        db.session.add(new_project)
        db.session.commit()
        return new_project.id

    def create_project_status(self, project, proj_id):
        for system_summary_id in project['summ_group']['summaries']:
            new_summ_status = ProjectStatus(
                summary_id=system_summary_id,
                eval_proj_id=proj_id,
                total_exp_results=project['total_exp_results'],
            )
            db.session.add(new_summ_status)
            db.session.commit()
