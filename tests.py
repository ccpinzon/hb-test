import json
import unittest
from services import properties_habi as api_habi


class RestAPITest(unittest.TestCase):

    def test_with_filters(self):
        body_json_str = '''
        {
            "filters": {
                "city": "medellin",
                "year": 2011,
                "status": "vendido"
            }
        }
        '''

        response = api_habi.get_habi_property_list(json.loads(body_json_str))

        self.assertEqual(True, True)  # add assertion here

    def test_with_filter_city(self):
        body_json_str = '''
        {
            "filters": {
                "city": "medellin"
            }
        }
        '''

        response = api_habi.get_habi_property_list(json.loads(body_json_str))
        print(f'response ==> ', json.dumps(response))

        self.assertEqual(True, True)  # add assertion here

    def test_with_filter_city_and_year(self):
        body_json_str = '''
        {
            "filters": {
                "city": "medellin",
                "year": 2011
            }
        }
        '''

        response = api_habi.get_habi_property_list(json.loads(body_json_str))

        self.assertTrue(response is not None)  # add assertion here

    def test_without_filters(self):
        body_json_str = '''
        {
            "filters": {
            }
        }
        '''

        response = api_habi.get_habi_property_list(json.loads(body_json_str))

        print(f'response ==> ', response)

        self.assertTrue(response is not None)

    def test_without_filters_empty(self):
        body_json_str = ''''''
        response = api_habi.get_habi_property_list(json.loads(body_json_str))

        print(f"RESPONSE -> ", response)
        self.assertEqual(True, True)  # add assertion here

    def test_query_filters(self):
        body_json_str = '''
        {
            "city": "medellin",
            "year": 2011,
            "status": "vendido"
        }
        '''
        json.loads(body_json_str)

        sql = api_habi.sql_with_filters("", json.loads(body_json_str))
        print(sql)
        self.assertTrue(sql is not None)  # add assertion here


if __name__ == '__main__':
    unittest.main()
