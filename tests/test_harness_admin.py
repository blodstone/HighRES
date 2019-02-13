import json
from flask_testing import TestCase
from backend.app import create_app
from backend.model.dataset import Dataset, DatasetSchema
from backend.model.project import EvaluationProject
from backend.model.summary import SummaryGroup, SummaryGroupSchema


class HarnessAdminTest(TestCase):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:wildanimus@localhost/harness_test"
    IS_INIT_DB = 1
    DATASET_PATH = '/home/acp16hh/Projects/Research/Experiments/Exp_Elly_Human_Evaluation/src/harness/dataset/BBC'

    def create_app(self):
        app = create_app(self, True)
        return app

    def create_proj(self):
        dataset = DatasetSchema().dump(Dataset.query.first())
        # dataset = '{"summ_groups": [{"summaries": [1], "dataset": 1, "is_ref": false, "name": "BBC_test_system_tconvs2s", "id": 1}, {"summaries": [2], "dataset": 1, "is_ref": false, "name": "BBC_test_system_ptgen", "id": 2}, {"summaries": [3], "dataset": 1, "is_ref": true, "name": "BBC_test_ref_gold", "id": 3}], "name": "BBC_test", "id": 1}'
        summ_group = SummaryGroupSchema().dump(SummaryGroup.query.first())
        # summ_group = '{"name": "BBC_test_system_ptgen", "dataset": 1, "summaries": [2], "is_ref": false, "id": 2}'
        return self.client.put(f"/admin/project/evaluation",
                        data=json.dumps(dict(
                            name='Test Create',
                            summ_group=summ_group.data,
                            dataset=dataset.data,
                            category='Fluency',
                            total_exp_results=1
                        )
                        ),
                        content_type='application/json'
                        )

    def test_setup(self):
        self.assertTrue(self.app is not None)

    def test_get_dataset(self):
        response = self.client.get('/admin/dataset')
        result = DatasetSchema(many=True, only=('id', 'name', 'summ_groups'))\
            .dump(Dataset.query.all())
        self.assert200(response)
        self.assertEqual(result.data, response.json)

    def test_create_project(self):
        response = self.create_proj()
        self.assert200(response)

    def test_get_fluency(self):
        self.create_proj()
        response = self.client.get(f"/fluency/1?n=5")
        print(response.json)
        self.assert200(response)
