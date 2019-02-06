"""
Initialize Flask Blueprint.
"""
from flask import Blueprint
api = Blueprint('api', 'api', url_prefix='', static_folder='../../instance/dist/static')
api.config = {}


@api.record
def record_params(setup_state):
    app = setup_state.app
    api.config = dict([(key, value) for (key, value) in app.config.items()])








