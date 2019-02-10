from flask_testing import TestCase
from backend.app import create_app
from backend.model.dataset import Dataset, DatasetSchema


class HarnessAdminTest(TestCase):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:wildanimus@localhost/harness_test"
    IS_INIT_DB = 0
    DATASET_PATH = '/home/acp16hh/Projects/Research/Experiments/Exp_Elly_Human_Evaluation/src/harness/dataset/BBC_test'

    def create_app(self):
        app = create_app(self, True)
        return app

    def test_setup(self):
        self.assertTrue(self.app is not None)

    def test_get_dataset(self):
        response = self.client.get('/admin/dataset')
        result = DatasetSchema(many=True, only=('name', 'summ_groups'))\
            .dump(Dataset.query.all())
        self.assert200(response)
        self.assertEqual(result.data, response.json)

