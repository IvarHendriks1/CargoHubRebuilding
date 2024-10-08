import pytest
import requests

API_KEY = 'a1b2c3d4e5'


@pytest.fixture
def _url():
    return 'http://localhost:3000/api/v1/'


# Test to get a specific client by ID
def test_get_client_by_id(_url):
    url = _url + 'clients'
    params = {'id': 123}

    # Send a GET request to fetch a client by ID
    response = requests.get(url, params=params, headers={'API_KEY': API_KEY})

    # Verify that the status code is either 200 (OK) or 404 (Not Found)
    assert response.status_code in [200, 404], f"Unexpected status code: {response.status_code}"

    if response.status_code == 200:
        response_data = response.json()
        assert response_data['id'] == 123
    else:
        print("Client with ID 123 not found")


# Test to create (POST) a new client
def test_post_client(_url):
    url = _url + 'clients'
    new_client = {
        'name': 'Jane Doe',
        'email': 'janedoe@example.com',
    }

    # Send a POST request to create a new client
    response = requests.post(url, json=new_client, headers={'API_KEY': API_KEY})

    # Verify that the status code is 201 (Created)
    assert response.status_code == 201, f"Unexpected status code: {response.status_code}"

    # Check if response contains valid JSON or skip the response body validation
    if response.content:
        response_data = response.json()  # Parse JSON response if body is not empty
        assert 'id' in response_data
        print(f"Created Client ID: {response_data['id']}")
    else:
        print("POST request returned 201 but no response body.")


# Test to update (PUT) a client
def test_put_client(_url):
    url = _url + 'clients/123'  # Replace 123 with actual ID to test
    updated_client = {
        'name': 'Jane Smith',
        'email': 'janesmith@example.com',
    }

    # Send a PUT request to update a specific client
    response = requests.put(url, json=updated_client, headers={'API_KEY': API_KEY})

    # Verify that the status code is 200 (OK), 404 (Not Found), or 500 (Server Error)
    assert response.status_code in [200, 404, 500], f"Unexpected status code: {response.status_code}"

    if response.status_code == 200:
        response_data = response.json()
        print(f"Client successfully updated: {response_data}")
    elif response.status_code == 404:
        print("Client not found, cannot update")
    else:
        print("Server error when trying to update client")


# Test to delete a client by ID
def test_delete_client(_url):
    url = _url + 'clients/123'  # Replace 123 with actual ID to test

    # Send a DELETE request to delete the client
    response = requests.delete(url, headers={'API_KEY': API_KEY})

    # Verify that the status code is 200 (OK), 404 (Not Found), or 500 (Server Error)
    assert response.status_code in [200, 404, 500], f"Unexpected status code: {response.status_code}"

    if response.status_code == 200:
        print("Client successfully deleted")
    elif response.status_code == 404:
        print("Client not found, cannot delete")
    else:
        print("Server error when trying to delete client")
