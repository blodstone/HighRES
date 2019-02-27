import urllib.parse
from flask import request
from flask_restful import Resource, abort
from backend.model.project import FluencyProject, FluencyProjectSchema
from backend.model.project_status import ProjectStatus
from backend.model import ma


class ProgressObject(object):
    def __init__(self, total, current):
        self.total = total
        self.current = current


class ProgressSchema(ma.Schema):
    class Meta:
        fields = ('total', 'current')


class FluencyUIObject(object):
    def __init__(self, no, project, link, progress):
        self.no = no
        self.project = project
        self.link = link
        self.progress = progress


class FluencyUISchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('no', 'project', 'link', 'progress')
    project = ma.Nested(FluencyProjectSchema)
    progress = ma.Nested(ProgressSchema)


class FluencyListResource(Resource):

    def __get_project_progress(self, project):
        total = ProjectStatus.query.filter_by(fluency_proj_id=project.id).count()
        current = ProjectStatus.query.filter_by(
            fluency_proj_id=project.id, is_finished=True).count()
        return ProgressObject(total=total, current=current)

    def get(self):
        projects = FluencyProject.query.all()
        if len(projects) == 0:
            return abort(404, message=f"No fluency projects.")
        else:
            schema = FluencyUISchema(many=True)
            fluency_ui_objs = []
            for no, project in enumerate(projects):
                progress = self.__get_project_progress(project)
                link = urllib.parse.urljoin(
                        request.host_url,
                        f"#/Fluency/{project.id}"
                        )
                fluency_ui_obj = FluencyUIObject(
                    no=no+1, project=project, link=link, progress=progress)
                fluency_ui_objs.append(fluency_ui_obj)
            return schema.dump(fluency_ui_objs)
            # result_json = {'projects': []}
            # for project in projects:
            #     project_json = project.to_dict()
            #     project_json['dataset_name'] = \
            #         Dataset.query.filter_by(id=project.dataset_id).first().name
            #     total_n_results = 0
            #     total_total_exp_results = 0
            #     if project_type == ProjectType.ANNOTATION.value.lower():
            #         for doc_status in project.doc_statuses:
            #             n_results = AnnotationResult.query \
            #                 .filter_by(status_id=doc_status.id).count()
            #             total_n_results += n_results
            #             total_total_exp_results += doc_status.total_exp_results
            #     elif project_type == ProjectType.EVALUATION.value.lower():
            #         for summ_status in project.summ_statuses:
            #             n_results = EvaluationResult.query \
            #                 .filter_by(status_id=summ_status.id).count()
            #             total_n_results += n_results
            #             total_total_exp_results += summ_status.total_exp_results
            #     project_json['progress'] = total_n_results / total_total_exp_results
            #     project_json['no'] = len(result_json['projects']) + 1
            #     if project_type.lower() == ProjectType.EVALUATION.value.lower():
            #         summ_group = SummaryGroup.query.get(project.summ_group_id)
            #         project_json['summ_group_name'] = summ_group.name
            #
            #     category = project.category.lower()
            #     if project.category.lower() == ProjectCategory.INFORMATIVENESS_DOC.value.lower():
            #         highlight = 1
            #     else:
            #         highlight = 0
            #     if project.category.lower() == ProjectCategory.INFORMATIVENESS_DOC_NO.value.lower() or \
            #             project.category.lower() == ProjectCategory.INFORMATIVENESS_DOC.value.lower():
            #         if project.category.lower() == ProjectCategory.INFORMATIVENESS_DOC_NO.value.lower():
            #             category = ProjectCategory.INFORMATIVENESS_DOC.value.lower()
            #         project_json['link'] = urllib.parse.urljoin(
            #             request.host_url,
            #             '#/{type}/{category}/{highlight}/{id}/1'.format(
            #                 type=project_type,
            #                 highlight=highlight,
            #                 category=category,
            #                 id=project_json['id']
            #             ))
            #     else:
            #         project_json['link'] = urllib.parse.urljoin(
            #             request.host_url,
            #             '#/{type}/{category}/{id}/1'.format(
            #                 type=project_type,
            #                 category=category,
            #                 id=project_json['id']
            #             ))
            #     result_json['projects'].append(project_json)
            # return jsonify(result_json)
