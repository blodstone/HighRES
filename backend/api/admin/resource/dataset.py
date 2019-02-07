from flask_restful import Resource

from backend.model.dataset import Dataset, DatasetSchema


class DatasetsResource(Resource):

    def get(self):
        datasets = Dataset.query.all()
        datasets_schema = DatasetSchema(many=True)
        result = datasets_schema.dump(datasets)
        return result


class DatasetResource(Resource):
    def get(self, id):
        dataset = Dataset.query.get(id)
        return DatasetSchema().dump(dataset)
