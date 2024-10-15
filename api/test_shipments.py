
import pytest
import requests

API_KEY = 'a1b2c3d4e5'


@pytest.fixture
def base_url():
    return 'http://localhost:3000/api/v1/'


# Test fetching a shipment by ID
def test_get_shipment_by_id(base_url):
    url = base_url + 'shipments/1' 

    response = requests.get(url, headers={'API_KEY': API_KEY})

    assert response.status_code in [200, 404]


# Test updating a shipment
def test_update_shipment_status(base_url):
    url = base_url + 'shipments/1'
    payload = {
        "id": 1,
        "shipment_status": "Shipped"
    }

    response = requests.put(url, headers={'API_KEY': API_KEY}, json=payload)

    # Verify if the shipment was updated
    assert response.status_code == 200



# Test updating shipment details
def test_update_shipment_details(base_url):
    url = base_url + 'shipments/1'
    payload = {
        "id": 1,
        "origin": "Utrecht",
        "weight": 450
    }

    response = requests.put(url, headers={'API_KEY': API_KEY}, json=payload)

    # Verify if the shipment was updated
    assert response.status_code == 200


# Test deleting a shipment
def test_delete_shipment(base_url):
    url = base_url + 'shipments/5'
   
    response = requests.delete(url, headers={'API_KEY': API_KEY})

    # Verify if the shipment was deleted successfully (204 No Content)
    assert response.status_code == 204

