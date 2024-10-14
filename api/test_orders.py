
import pytest
import requests

API_KEY = 'a1b2c3d4e5'


@pytest.fixture
def _url():
    return 'http://localhost:3000/api/v1/'


# Test to create an order with a specified ID
def test_create_order(_url):
    url = _url + 'orders'
    new_order = {
        "id": 7000,  # Specifying a unique ID
        "source_id": 33,
        "order_date": "2019-04-03T11:33:15Z",
        "request_date": "2019-04-07T11:33:15Z",
        "reference": "ORD00001",
        "reference_extra": "Bedreven arm straffen bureau.",
        "order_status": "Delivered",
        "notes": "Voedsel vijf vork heel.",
        "shipping_notes": "Buurman betalen plaats bewolkt.",
        "picking_notes": "Ademen fijn volgorde scherp aardappel op leren.",
        "warehouse_id": 18,
        "shipment_id": 1,
        "total_amount": 9905.13,
        "total_discount": 150.77,
        "total_tax": 372.72,
        "total_surcharge": 77.6,
        "items": [
            {"item_id": "P007435", "amount": 23},
            {"item_id": "P009557", "amount": 1}
        ]
    }

    # Send a POST request to create the order
    response = requests.post(url, json=new_order, headers={'API_KEY': API_KEY})

    # Check if the status code is 201 (Created)
    assert response.status_code == 201, f"Unexpected status code: {response.status_code}"

    # Only attempt to parse response if content is available
    if response.content:
        response_data = response.json()  # Parse JSON if content is present
        # Verify the response contains the correct ID
        assert response_data['id'] == new_order['id'], "Order creation response should contain the correct 'id'"
        order_id = response_data['id']
    else:
        print("Response has no content. Skipping JSON parsing.")
        order_id = new_order['id']

    return order_id  # Return the order ID for use in other tests



def test_update_order(_url):
    order_id = test_create_order(_url)  # Create an order and get its ID
    url = _url + f'orders/{order_id}'  # Use the order ID in the URL
    updated_order = {
        "order_status": "Shipped",  # Only updating the order status
    }

    # Send a PUT request to update the order
    response = requests.put(url, json=updated_order, headers={'API_KEY': API_KEY})

    # Verify the status code is 200 (OK)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    # Check if the response reflects the updates
    response_data = response.json()
    assert response_data['order_status'] == "Shipped", "Order status did not update"


# Test to fetch an order by ID
def test_get_order_by_id(_url):
    order_id = test_create_order(_url)  # Create an order and get its ID
    url = _url + f'orders/{order_id}'  # Use the order ID in the URL

    # Send a GET request to fetch the order by ID
    response = requests.get(url, headers={'API_KEY': API_KEY})

    # Verify the status code is 200 (OK)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    # Validate response data
    order_data = response.json()
    assert order_data['reference'] == "ORD00001", "Order reference does not match"
    assert order_data['order_status'] == "Delivered", "Order status does not match"


# Test to delete an order by ID
def test_delete_order(_url):
    order_id = test_create_order(_url)  # Create an order and get its ID
    url = _url + f'orders/{order_id}'  # Use the order ID in the URL

    # Send a DELETE request to delete the order
    response = requests.delete(url, headers={'API_KEY': API_KEY})

    # Verify the status code is 204 (No Content)
    assert response.status_code == 204, f"Unexpected status code: {response.status_code}"


# Test to fetch all orders
def test_fetch_all_orders(_url):
    url = _url + 'orders'

    # Send a GET request to fetch all orders
    response = requests.get(url, headers={'API_KEY': API_KEY})

    # Verify the status code is 200 (OK)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    # Check if the response is a list of orders
    orders = response.json()
    assert isinstance(orders, list), "Expected a list of orders"
    assert len(orders) > 0, "Expected at least one order"


# Test to create an order with missing required fields (invalid creation)
def test_create_order_invalid(_url):
    url = _url + 'orders'
    invalid_order = {
        # Missing important fields like source_id, reference, etc.
        "id": 7001,
        "order_status": "Delivered"
    }

    # Send a POST request with invalid data
    response = requests.post(url, json=invalid_order, headers={'API_KEY': API_KEY})

    # Verify the status code is 400 (Bad Request)
    assert response.status_code == 400, f"Expected 400 error, got: {response.status_code}"
