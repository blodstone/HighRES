import urllib.parse
from flask import request
from flask_restful import Resource, abort
from backend.model.project import ClarityProject, ClarityProjectSchema
from backend.model.project_status import ProjectStatus
from backend.model import ma


class ProgressObject(object):
    def __init__(self, total, current):
        self.total = total
        self.current = current


class ProgressSchema(ma.Schema):
    class Meta:
        fields = ('total', 'current')


class ClarityUIObject(object):
    def __init__(self, no, project, link, progress):
        self.no = no
        self.project = project
        self.link = link
        self.progress = progress


class ClarityUISchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('no', 'project', 'link', 'progress')
    project = ma.Nested(ClarityProjectSchema)
    progress = ma.Nested(ProgressSchema)


class ClarityListResource(Resource):

    def __get_project_progress(self, project):
        total = ProjectStatus.query.filter_by(clarity_proj_id=project.id).count()
        current = ProjectStatus.query.filter_by(
            clarity_proj_id=project.id, is_finished=True).count()
        return ProgressObject(total=total, current=current)

    def get(self):
        projects = ClarityProject.query.all()
        if len(projects) == 0:
            return abort(404, message=f"No clarity projects.")
        else:
            schema = ClarityUISchema(many=True)
            clarity_ui_objs = []
            for no, project in enumerate(projects):
                progress = self.__get_project_progress(project)
                link = urllib.parse.urljoin(
                        request.host_url,
                        f"#/Clarity/{project.id}"
                        )
                clarity_ui_obj = ClarityUIObject(
                    no=no+1, project=project, link=link, progress=progress)
                clarity_ui_objs.append(clarity_ui_obj)
            return schema.dump(clarity_ui_objs)
