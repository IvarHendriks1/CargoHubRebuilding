import pytest
import requests

API_KEY = 'a1b2c3d4e5'


@pytest.fixture
def _url():
    return 'http://localhost:3000/api/v1/'
        
def test_client_lifecycle(_url):
    url = _url + 'clients'
    
    # Step 1: Create a client
    new_client = {
        'id': 9999,
        'name': 'John Doe',
        'contact_email': 'johndoe@example.com'
    }
    response = requests.post(url, json=new_client, headers={'API_KEY': API_KEY})
    
    print(f"Response status: {response.status_code}")
    print(f"Response body: {response.text}")
    
    # Check if the status code is 201 (Created)
    assert response.status_code == 201, "Client creation failed"
    
def test_fetch_created_client(_url):
    url = _url + 'clients'

    # Step 1: Create a client
    new_client = {
        'id': 9999,
        'name': 'John Doe',
        'contact_email': 'johndoe@example.com'
    }
    response = requests.post(url, json=new_client, headers={'API_KEY': API_KEY})
    assert response.status_code == 201, "Client creation failed"
    
    # Extract client ID if present
    client_id = 9999
    if response.content:
        client_id = response.json().get('id')
    
    if client_id:
        # Step 2: Fetch the created client by ID
        response = requests.get(f"{url}/{client_id}", headers={'API_KEY': API_KEY})
        assert response.status_code == 200, "Failed to fetch created client"
        fetched_client = response.json()
        assert fetched_client['name'] == 'John Doe', "Client name mismatch"
    else:
        print("No client ID returned, skipping fetch.")


def test_fetch_nonexistent_client(_url):
    url = _url + 'clients/99999'  
    response = requests.get(url, headers={'API_KEY': API_KEY})
    assert response.status_code == 404, f"Expected 404, got: {response.status_code}"

def test_update_client_invalid_data(_url):
    url = _url + 'clients/123' 
    invalid_data = {'contact_email': 'invalid-email'}  
    response = requests.put(url, json=invalid_data, headers={'API_KEY': API_KEY})
    assert response.status_code == 400, f"Expected 400 for invalid email, got: {response.status_code}"

def test_delete_nonexistent_client(_url):
    url = _url + 'clients/99999'  
    response = requests.delete(url, headers={'API_KEY': API_KEY})
    assert response.status_code == 404, f"Expected 404, got: {response.status_code}"

def test_fetch_all_clients(_url):
    url = _url + 'clients'
    response = requests.get(url, headers={'API_KEY': API_KEY})
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert isinstance(response.json(), list), "Expected a list of clients"

def test_fetch_client_by_email(_url):
    # Step 1: Create a client to test with
    url = _url + 'clients'
    new_client = {
        'id': 5839,
        'name': 'John Doe',
        'contact_email': 'johndoe@example.com'}
    response = requests.post(url, json=new_client, headers={'API_KEY': API_KEY})
    client_id = response.json()['id']

    # Step 2: Fetch the client by email
    params = {'contact_email': 'johndoe@example.com'}
    response = requests.get(url, params=params, headers={'API_KEY': API_KEY})
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert response.json()['contact_email'] == 'johndoe@example.com', "Email doesn't match"

def test_partial_update_client(_url):
    url = _url + 'clients/1'
    partial_update = {'name': 'Test'}  # Only update name
    response = requests.put(url, json=partial_update, headers={'API_KEY': API_KEY})
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert response.json()['name'] == 'Test', "name didn't update"

def test_client_id_field_validation(_url):
    invalid_id = 'abc'  # Non-numeric client ID
    url = _url + f'clients/{invalid_id}'
    response = requests.get(url, headers={'API_KEY': API_KEY})
    assert response.status_code == 400, f"Expected 400 for invalid ID, got: {response.status_code}"

def test_create_multiple_clients_and_fetch(_url):
    url = _url + 'clients'

    # Step 1: Create multiple clients
    client1 = {'name': 'Client One', 'contact_email': 'client1@example.com'}
    client2 = {'name': 'Client Two', 'email': 'client2@example.com'}
    requests.post(url, json=client1, headers={'API_KEY': API_KEY})
    requests.post(url, json=client2, headers={'API_KEY': API_KEY})

    # Step 2: Fetch all clients and verify the two were created
    response = requests.get(url, headers={'API_KEY': API_KEY})
    clients = response.json()
    assert len(clients) >= 2, "Expected at least 2 clients in the list"


