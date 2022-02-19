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

        response = api_habi.get_habi_property_list(body_json_str)

        self.assertEqual(True, True)  # add assertion here

    def test_with_filter_city(self):
        body_json_str = '''
        {
            "filters": {
                "city": "medellin"
            }
        }
        '''

        response = api_habi.get_habi_property_list(body_json_str)

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

        response = api_habi.get_habi_property_list(body_json_str)

        self.assertEqual(True, True)  # add assertion here

    def test_without_filters(self):
        body_json_str = '''
        {
            "filters": {
            }
        }
        '''

        response = api_habi.get_habi_property_list(body_json_str)

        self.assertEqual(True, True)  # add assertion here

    def test_without_filters_empty(self):
        body_json_str = '''
        '''

        response = api_habi.get_habi_property_list(body_json_str)

        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
