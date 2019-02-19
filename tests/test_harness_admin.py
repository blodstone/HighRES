import json
import random
import string
from flask_testing import TestCase
from backend.app import create_app
from backend.model.dataset import Dataset, DatasetSchema
from backend.model.summary import SummaryGroup, SummaryGroupSchema
from backend.model.result import FluencyResultSchema, FluencyResult


class HarnessAdminTest(TestCase):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:wildanimus@localhost/harness_test"
    IS_INIT_DB = 1
    DATASET_PATH = '/home/acp16hh/Projects/Research/Experiments/Exp_Elly_Human_Evaluation/src/harness/dataset/BBC'

    def create_app(self):
        app = create_app(self, True)
        return app

    def __create_proj(self):
        summ_group_list = SummaryGroupSchema().dump(SummaryGroup.query.limit(3), many=True)
        return self.client.put(f"/admin/project/evaluation",
                        data=json.dumps(dict(
                            name='Test Create',
                            summ_group_list=summ_group_list.data,
                            category='Fluency',
                            n_summaries=5,
                            expire_duration=3
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
        response = self.__create_proj()
        self.assert200(response)

    def test_get_fluency(self):
        self.__create_proj()
        response = self.client.get(f"/fluency/1")
        self.assert200(response)
        results = response.json['results']
        self.assertTrue('results' in response.json)
        self.assertTrue('summaries' in response.json)
        self.assertTrue('proj_status' in response.json)
        self.assertTrue('sanity_summ' in response.json)
        self.assertEqual(len(results), 5)
        self.assertNotEqual(len(results), 4)

    def test_post_fluency(self):
        self.__create_proj()
        response = self.client.get(f"/fluency/1?n=5")
        results = response.json['results']
        results_schema = FluencyResultSchema(many=True)
        for result in results:
            result['fluency'] = 1
            result['clarity'] = 100
        results_schema.dump(results)
        response = self.client.post(f"/fluency/1",
                                    data=json.dumps(results_schema.dump(results).data),
                                    content_type='application/json')
        for result in results:
            result_query = FluencyResult.query.get(result['id'])
            self.assertEqual(result_query.fluency, result['fluency'])
            self.assertEqual(result_query.clarity, result['clarity'])
        self.assert200(response)
