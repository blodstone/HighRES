"""
Initialize Flask Blueprint for admin api.
"""
from flask import Blueprint
from flask_restful import Api
from .resource.fluency import DatasetsResource, FluencyResource
from .resource.fluencylist import FluencyListResource

admin_api = Blueprint('admin_api', __name__, static_folder='../../instance/dist/static')
admin_api.config = {}
api = Api()
api.init_app(admin_api)
api.add_resource(DatasetsResource, '/dataset')
api.add_resource(FluencyResource, '/fluency', '/fluency/<int:project_id>')
api.add_resource(FluencyListResource, '/fluencylist')


@admin_api.record
def record_params(setup_state):
    """
    Copy flask app config into the api config
    """
    app = setup_state.app
    admin_api.config = dict([(key, value) for (key, value) in app.config.items()])





