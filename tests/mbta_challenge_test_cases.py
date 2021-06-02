import unittest
import requests

from mbta_challenge import get_subway_routes_long_names

class MbtaTestCase(unittest.TestCase):
    """Tests for """
    def test_api_status_code(self):
        """Can we connect to API server?"""
        # Connect to entire API
        mbta_api_url = requests.get('https://api-v3.mbta.com')
        mbta_api_url_status = mbta_api_url.status_code
        self.assertEqual(mbta_api_url_status, 200)

        # Connect using params and filters
        mbta_api_url_with_params_and_filters = requests.get('https://api-v3.mbta.com/routes/?fields%5Broute%5D=long_name&filter[type]=0,1')

if __name__ == '__main__':
    unittest.main()