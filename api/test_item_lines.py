import pytest
import requests

API_KEY = 'a1b2c3d4e5'


@pytest.fixture
def _url():
    return 'http://localhost:3000/api/v1/'


def test_post_item_lines(_url):
    
    url = _url + 'item_lines'
    payload = {
    "id": 6942069,
    "name": "Tech Gadgets",
    "description": "dikke"
    }

    # Send a POST request to the API
    response = requests.post(url, headers={'API_KEY': API_KEY}, json=payload)

    # Get the status code
    status_code = response.status_code

    # Verify that the status code is 404 (not found)
    # It needs to get a 404 because a POST request shouldnt be possible
    assert status_code == 404

def test_get_item_lines_by_id(_url):
    url = _url + 'item_lines'
    params = {'id': '1'}

    # Send a GET request to fetch a item lines by ID
    response = requests.get(url, params=params, headers={'API_KEY': API_KEY})

    # Verify that the status code is either 200 (OK) or 404 (Not Found)
    assert response.status_code in [200, 404], f"Unexpected status code: {response.status_code}"

    if response.status_code == 200:
        response_data = response.json()
        assert response_data['name'] == 'Tech Gadgets'
    else:
        print("Item lines with name Tech Gadgets not found")

def test_put_item_lines(_url):
    url = _url + 'item_lines/1'
    
    updated_payload = {
    "id": 1,
    "name": "Home Appliances",
    "description": "UPDATED"
    }

    try:
        # Send a PUT request to update the specific item
        response = requests.put(url, json=updated_payload, headers={'API_KEY': API_KEY})

        # Verify that the status code is 200 (OK), 404 (Not Found), or 500 (Server Error)
        assert response.status_code in [200, 404, 500], f"Unexpected status code: {response.status_code}"

        if response.status_code == 200:
            response_data = response.json()
            print(f"Item lines successfully updated: {response_data}")
        elif response.status_code == 404:
            print("Item lines not found, cannot update")
        else:
            print("Server error when trying to update item lines")
    
    # Catch any requests-related errors, including timeouts
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def test_get_item_lines_by(_url):
    url = _url + 'item_lines'
    params = {'id': '1'}

    # Send a GET request to fetch a item line by ID
    response = requests.get(url, params=params, headers={'API_KEY': API_KEY})

    # Verify that the status code is either 200 (OK) or 404 (Not Found)
    assert response.status_code in [200, 404], f"Unexpected status code: {response.status_code}"

    if response.status_code == 200:
        response_data = response.json()
        assert response_data['description'] == 'UPDATED'
    else:
        print("Item lines with description UPDATED not found")

def test_delete_item_lines_by(_url):
    url = _url + 'item_lines'
    params = {'id': '1'}

    # Send a DELETE request to delete a item lines by ID
    response = requests.delete(url, params=params, headers={'API_KEY': API_KEY})

    # Verify that the status code is either 200 (OK) or 404 (Not Found)
    assert response.status_code in [200, 404], f"Unexpected status code: {response.status_code}"

    
def test_get_all_item_lines(_url):
    url = _url + 'item_lines'

    # Send a GET request to fetch all item lines
    response = requests.get(url, headers={'API_KEY': API_KEY})

    # Verify that the status code is either 200 (OK) or 404 (Not Found)
    assert response.status_code in [200, 404], f"Unexpected status code: {response.status_code}"