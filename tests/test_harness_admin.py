import json
import random
import string
from flask_testing import TestCase
from backend.app import create_app
from backend.model.dataset import Dataset, DatasetSchema
from backend.model.summary import SummaryGroup, SummaryGroupSchema
from backend.model.result import FluencyResult
from backend.model.project_status import ProjectStatus


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
        return self.client.put(f"/admin/fluency",
                        data=json.dumps(dict(
                            name='Test Create',
                            summ_group_list=summ_group_list.data,
                            category='Fluency',
                            n_summaries=5,
                            expire_duration=3,
                            total_exp_results=2
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
        res_sums = response.json['res_sums']
        self.assertTrue('res_sums' in response.json)
        self.assertTrue('proj_status' in response.json)
        self.assertTrue('sanity_summ' in response.json)
        self.assertEqual(len(res_sums), 5)
        self.assertNotEqual(len(res_sums), 4)
        response = self.client.delete(f"/admin/fluency/1")
        self.assert200(response)
        response = self.client.get(f"/fluency/1")
        self.assert404(response)

    def test_post_fluency(self):
        self.__create_proj()
        response = self.client.get(f"/fluency/1")
        # Edit the results
        res_sums = response.json['res_sums']
        results = [res_sum['result'] for res_sum in res_sums]
        for result in results:
            result['fluency'] = 1
            result['clarity'] = 100
        # Edit the proj status
        proj_status = response.json['proj_status']
        proj_status['validity'] = True
        proj_status['is_finished'] = True
        proj_status['is_active'] = False

        response = self.client.post(f"/fluency",
                                    data=json.dumps({
                                        'results': results,
                                        'proj_status': proj_status
                                    }),
                                    content_type='application/json')
        self.assert200(response)
        for result in results:
            result_query = FluencyResult.query.get(result['id'])
            self.assertEqual(result_query.fluency, result['fluency'])
            self.assertEqual(result_query.clarity, result['clarity'])

        proj_status_query = ProjectStatus.query.get(proj_status['id'])
        self.assertEqual(proj_status_query.validity, proj_status['validity'])
        self.assertEqual(proj_status_query.is_finished, proj_status['is_finished'])
        self.assertEqual(proj_status_query.is_active, proj_status['is_active'])
        response = self.client.delete(f"/admin/fluency/1")
        self.assert200(response)
