from flask_testing import TestCase
from backend.app import create_app, init_db
from backend.model import db
from backend.model.dataset import Dataset, DatasetSchema


class HarnessTest(TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        app = create_app(self, True)
        return app

    def setUp(self):
        db_config = {
            'init_dataset': 1,
            'dataset_path': '/home/acp16hh/Projects/Research/Experiments/Exp_Elly_Human_Evaluation/src/harness/dataset/BBC'
        }
        init_db(db_config)
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
        response = self.client.get('/dataset/2')
        self.assertEqual(404, response.status_code)
