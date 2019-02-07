from flask_testing import TestCase
from backend.app import create_app
from backend.model import db
from backend.model.dataset import Dataset, DatasetSchema


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

    def test_get_datasets_admin(self):
        response = self.client.get('/admin/dataset')
        result = DatasetSchema(many=True).dump(Dataset.query.all())
        self.assertEqual(result.data, response.json)

    def test_get_dataset_admin(self):
        response = self.client.get('/admin/dataset/1')
        result = DatasetSchema().dump(Dataset.query.get(1))
        self.assertEqual(result.data, response.json)

    def test_get_datasets_user(self):
        response = self.client.get('/dataset')
        result = DatasetSchema(many=True).dump(Dataset.query.all())
        self.assertEqual(result.data, response.json)

    def test_get_dataset_user(self):
        response = self.client.get('/dataset/1')
        result = DatasetSchema().dump(Dataset.query.get(1))
        self.assertEqual(result.data, response.json)
