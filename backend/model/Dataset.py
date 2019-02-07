from backend.model import db, ma
from flask_restful import Resource


class Dataset(db.Model):
    __tablename__ = 'dataset'
    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)


class DatasetSchema(ma.ModelSchema):
    class Meta:
        model = Dataset


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
