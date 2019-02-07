from flask_restful import Resource, abort

from backend.model.dataset import Dataset, DatasetSchema


class DatasetsResource(Resource):

    def get(self):
        datasets = Dataset.query.all()
        datasets_schema = DatasetSchema(many=True)
        if len(datasets) > 0:
            return datasets_schema.dump(datasets)
        else:
            abort(404, message='Empty datasets')


class DatasetResource(Resource):
    def get(self, dataset_id):
        dataset = Dataset.query.get(dataset_id)
        if dataset:
            return DatasetSchema().dump(dataset)
        else:
            abort(404, message="Dataset {} doesn't exist".format(dataset_id))
