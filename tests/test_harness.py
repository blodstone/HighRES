from flask_testing import TestCase
from backend.app import create_app
from backend.model import db, ma
from backend.model.Dataset import Dataset, DatasetSchema


class HarnessTest(TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        app = create_app(self, True)
        return app

    def setUp(self):
        db.create_all()
        dataset = Dataset(name="test_dataset")
        db.session.add(dataset)
        db.session.commit()

    def test_setup(self):
        self.assertTrue(self.app is not None)

    def test_get_datasets(self):
        response = self.client.get('/dataset')
        result = DatasetSchema(many=True).dump(Dataset.query.all())
        self.assertEquals(response.json, result.data)
