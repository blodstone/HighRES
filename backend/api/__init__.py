"""
Initialize Flask Blueprint for api.
"""
from flask import Blueprint
from backend.model import api
from backend.model.Dataset import DatasetResource

bp_api = Blueprint('api', 'api', url_prefix='', static_folder='../../instance/dist/static')
bp_api.config = {}
api.init_app(bp_api)
api.add_resource(DatasetResource, '/dataset')


@bp_api.record
def record_params(setup_state):
    """
    Copy flask app config into the api config
    """
    app = setup_state.app
    bp_api.config = dict([(key, value) for (key, value) in app.config.items()])


# from .dataset_api import *






