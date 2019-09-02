import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_initdata import test_data

class AddEventTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/add_event/"
    def tearDown(self):
        print(self.result)
    def test_addEvent_all_null(self):
        #所有参数为空
        payload = {'eid':'','':'','limit':'','address':'','start_time':''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_addEvent_eid_exist(self):
        payload = {'eid': 1, 'name': '一加4发布会', 'limit': 2000, 'address': '深圳宝体', 'start_time': '2017'}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event id already')
    def test_addEvent_name_exist(self):
        payload = {'eid': 12, 'name': '红米Pro发布会', 'limit': 2000, 'address': '深圳宝体', 'start_time': '2017'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event name already exists')
    def test_addEvent_dataType_error(self):
        payload = {'eid': 12, 'name': '一加5发布会', 'limit': 2000, 'address': '深圳宝体', 'start_time': 'tetr'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertIn('start_time format error.', self.result['message'])
    def test_addEvent_success(self):
        payload = {'eid': 12, 'name': '一加5发布会', 'limit': 2000, 'address': '深圳宝体', 'start_time': '2019-11-14 14:00:00'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add event success')

if __name__ == '__main__':
    test_data.init_data()
    unittest.main()

