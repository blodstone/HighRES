from flask_restful import Resource, abort

from backend.model.dataset import Dataset, DatasetSchema
from backend.model.summary import SummaryGroup, SummaryGroupSchema
from backend.model import db, ma


class DatasetsResource(Resource):

    def get(self):
        result = Dataset.query.all()
        schema = DatasetSchema(many=True, only=('name', 'summ_groups'))
        if len(result) > 0:
            return schema.dump(result)
        else:
            abort(404, message='Empty datasets or summary groups!')
