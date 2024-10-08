

import pytest
import requests


@pytest.fixture
def _url():
    return 'http://localhost:3000/api/v1/'


class Test_items:
    def test_get_items(_url):
        url = _url + 'items'

        # Send a GET request to the API
        response = requests.get(url)

        # Get the status code and response data
        status_code = response.status_code
        #response_data = response.json()

        # Verify that the status code is 200 (OK)
        assert status_code == 200

        # Verify the response data
    

    def test_get_item_by_id(_url):
        url = _url + 'items'
        params = {'id': 123}

        # Send a GET request to the API
        response = requests.get(url, params=params)

        # Get the status code and response data
        status_code = response.status_code
        response_data = response.json()

        # Verify that the status code is 200 (OK)
        assert status_code == 200

        # Verify the response data
        assert response_data['id'] == 123
        assert response_data['name'] == 'John Smith'


