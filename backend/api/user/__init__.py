"""
Initialize Flask Blueprint for user api.
"""
from flask import Blueprint
from flask_restful import Api
from .resource.dataset import DatasetsResource, DatasetResource

user_api = Blueprint('user_api', __name__)
user_api.config = {}
api = Api()
api.init_app(user_api)
api.add_resource(DatasetsResource, '/dataset')
api.add_resource(DatasetResource, '/dataset/<int:dataset_id>')


@user_api.record
def record_params(setup_state):
    """
    Copy flask app config into the api config
    """
    app = setup_state.app
    user_api.config = dict([(key, value) for (key, value) in app.config.items()])





