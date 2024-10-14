import pytest
import requests

API_KEY = 'a1b2c3d4e5'


@pytest.fixture
def _url():
    return 'http://localhost:3000/api/v1/'

   
def test_post_item(_url):
    
    url = _url + 'items'
    payload = {
    "uid": "P6942069",
    "code": "sjQ23408K",
    "description": "POST",
    "short_description": "must",
    "upc_code": "6523540947122",
    "model_number": "63-OFFTq0T",
    "commodity_code": "oTo304",
    "item_line": 11,
    "item_group": 73,
    "item_type": 14,
    "unit_purchase_quantity": 47,
    "unit_order_quantity": 13,
    "pack_order_quantity": 11,
    "supplier_id": 34,
    "supplier_code": "SUP423",
    "supplier_part_number": "E-86805-uTM"
    }

    # Send a POST request to the API
    response = requests.post(url, headers={'API_KEY': API_KEY}, json=payload)

    # Get the status code
    status_code = response.status_code

    # Verify that the status code is 201 (Created)
    assert status_code == 201


def test_get_item_by_id(_url):
    url = _url + 'items'
    params = {'uid': 'p6942069'}

    # Send a GET request to fetch a item by ID
    response = requests.get(url, params=params, headers={'API_KEY': API_KEY})

    # Verify that the status code is either 200 (OK) or 404 (Not Found)
    assert response.status_code in [200, 404], f"Unexpected status code: {response.status_code}"

    if response.status_code == 200:
        response_data = response.json()
        assert response_data['description'] == 'POST'
    else:
        print("Item with description POST not found")

def test_put_item(_url):
    url = _url + 'items/P6942069'
    
    updated_payload = {
    "uid": "P6942069",
    "code": "sjQ23408K",
    "description": "UPDATED",
    "short_description": "must",
    "upc_code": "6523540947122",
    "model_number": "63-OFFTq0T",
    "commodity_code": "oTo304",
    "item_line": 11,
    "item_group": 73,
    "item_type": 14,
    "unit_purchase_quantity": 47,
    "unit_order_quantity": 13,
    "pack_order_quantity": 11,
    "supplier_id": 34,
    "supplier_code": "SUP423",
    "supplier_part_number": "E-86805-uTM"
    }

    try:
        # Send a PUT request to update the specific item
        response = requests.put(url, json=updated_payload, headers={'API_KEY': API_KEY})

        # Verify that the status code is 200 (OK), 404 (Not Found), or 500 (Server Error)
        assert response.status_code in [200, 404, 500], f"Unexpected status code: {response.status_code}"

        if response.status_code == 200:
            response_data = response.json()
            print(f"Item successfully updated: {response_data}")
        elif response.status_code == 404:
            print("Item not found, cannot update")
        else:
            print("Server error when trying to update item")
    
    # Catch any requests-related errors, including timeouts
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def test_get_item_by(_url):
    url = _url + 'items'
    params = {'uid': 'p6942069'}

    # Send a GET request to fetch a item by ID
    response = requests.get(url, params=params, headers={'API_KEY': API_KEY})

    # Verify that the status code is either 200 (OK) or 404 (Not Found)
    assert response.status_code in [200, 404], f"Unexpected status code: {response.status_code}"

    if response.status_code == 200:
        response_data = response.json()
        assert response_data['description'] == 'UPDATED'
    else:
        print("Item with description UPDATED not found")

def test_delete_item_by(_url):
    url = _url + 'items'
    params = {'uid': 'p6942069'}

    # Send a DELETE request to delete a item by ID
    response = requests.delete(url, params=params, headers={'API_KEY': API_KEY})

    # Verify that the status code is either 200 (OK) or 404 (Not Found)
    assert response.status_code in [200, 404], f"Unexpected status code: {response.status_code}"

    
def test_get_all_items(_url):
    url = _url + 'items'

    # Send a GET request to fetch all items
    response = requests.get(url, headers={'API_KEY': API_KEY})

    # Verify that the status code is either 200 (OK) or 404 (Not Found)
    assert response.status_code in [200, 404], f"Unexpected status code: {response.status_code}"



# The same test only for the inventory of an item

# you can POST but it just doesnt POST it correct so this gives an 200 code
# but it shouldnt!!!!!!!!
# you can see it because when i PUT this inventory and change something it gives an good code (200) but 
# it doesnt change anything
def test_post_item_inventory(_url):
    
    url = _url + 'items/P000002/inventory'
    payload = {
        "id": 2,
        "item_id": "P000002",
        "description": "Focused transitional alliance",
        "item_reference": "nyg48736S",
        "locations": [
        19800,
        23653,
        3068,
        3334,
        20477,
        20524,
        17579,
        2271,
        2293,
        22717
        ],
        "total_on_hand": 194,
        "total_expected": 0,
        "total_ordered": 139,
        "total_allocated": 0,
        "total_available": 55
    }
    

    # Send a POST request to the API
    response = requests.post(url, json=payload, headers={'API_KEY': API_KEY})

    # Get the status code
    status_code = response.status_code

    # Verify that the status code is 201 (Created)
    assert status_code == 201


def test_get_item_inventory_by_id(_url):
    url = _url + 'items/P000002/inventory'

    # Send a GET request to fetch a item in inventory by ID
    response = requests.get(url, headers={'API_KEY': API_KEY})

    # Verify that the status code is either 200 (OK) or 404 (Not Found)
    assert response.status_code in [200, 404], f"Unexpected status code: {response.status_code}"

    if response.status_code == 200:
        response_data = response.json()

        # Handle the case where the response is a list
        if isinstance(response_data, list) and response_data:
            response_data = response_data[0]  # Access the first item if it's a list

        # Assert 'total_on_hand' exists and is correct
        assert response_data.get('total_on_hand') == 194
    else:
        print("Item not found.")


def test_put_item_inventory(_url):
    url = _url + 'items/P000002/inventory'
    
    updated_payload = [
    {
        "id": 2,
        "item_id": "P000002",
        "description": "UPDATED",
        "item_reference": "nyg48736S",
        "locations": [
        19800,
        23653,
        3068,
        3334,
        20477,
        20524,
        17579,
        2271,
        2293,
        22717
        ],
        "total_on_hand": 195,
        "total_expected": 0,
        "total_ordered": 139,
        "total_allocated": 0,
        "total_available": 55
    }
    ]

    try:
        # Send a PUT request to update the specific item
        response = requests.put(url, json=updated_payload, headers={'API_KEY': API_KEY})

        # Verify that the status code is 200 (OK), 404 (Not Found), or 500 (Server Error)
        assert response.status_code in [200, 404, 500], f"Unexpected status code: {response.status_code}"

        if response.status_code == 200:
            response_data = response.json()
            print(f"Item successfully updated: {response_data}")
        elif response.status_code == 404:
            print("Item not found, cannot update")
        else:
            print("Server error when trying to update item")
    
    # Catch any requests-related errors, including timeouts
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


# here above you PUT it but the PUT doenst change so this fails
# assert response_data.get('total_on_hand') == 195 fails 
def test_get_item_inevntory_by_(_url):
    url = _url + 'items/P000002/inventory'

    # Send a GET request to fetch a item in inventory by ID
    response = requests.get(url, headers={'API_KEY': API_KEY})

    # Verify that the status code is either 200 (OK) or 404 (Not Found)
    assert response.status_code in [200, 404], f"Unexpected status code: {response.status_code}"

    if response.status_code == 200:
        response_data = response.json()

        # Handle the case where the response is a list
        if isinstance(response_data, list) and response_data:
            response_data = response_data[0]  # Access the first item if it's a list

        # Assert 'total_on_hand' exists and is correct
        assert response_data.get('total_on_hand') == 195
    else:
        print("Item not found.")

def test_delete_item_inventory_by(_url):
    url = _url + 'items/P000002/inventory'

    # Send a DELETE request to delete a item by ID
    response = requests.delete(url, headers={'API_KEY': API_KEY})

    # Verify that the status code is 500 (Internal Server Error) because deleting this isnt possible
    assert response.status_code in [500], f"Unexpected status code: {response.status_code}"



# Test that should fail


# this payload misses an field that should be required
# so when the code is refectord it should give an 400 
def test_post_item_with_missing_field(_url):
    
    url = _url + 'items'
    payload = {
    "uid": "P6942069",
    "code": "sjQ23408K",
    "description": "POST",
    "short_description": "must",
    "upc_code": "6523540947122",
    "model_number": "63-OFFTq0T",
    "commodity_code": "oTo304",
    "item_group": 73,
    "item_type": 14,
    "unit_purchase_quantity": 47,
    "unit_order_quantity": 13,
    "pack_order_quantity": 11,
    "supplier_id": 34,
    "supplier_code": "SUP423",
    "supplier_part_number": "E-86805-uTM"
    }

    # Send a POST request to the API
    response = requests.post(url, headers={'API_KEY': API_KEY}, json=payload)

    # Get the status code
    status_code = response.status_code

    # Verify that the status code is 400 (Bad Request)
    assert status_code == 400



# this updated_payload misses an field that should be required
# so when the code is refectord it should give an 400 
def test_put_item_with_missing_field(_url):
    url = _url + 'items/P6942069'
    
    updated_payload = {
    "uid": "P6942069",
    "code": "sjQ23408K",
    "description": "UPDATED",
    "short_description": "must",
    "upc_code": "6523540947122",
    "model_number": "63-OFFTq0T",
    "commodity_code": "oTo304",
    "item_group": 73,
    "item_type": 14,
    "unit_purchase_quantity": 47,
    "unit_order_quantity": 13,
    "pack_order_quantity": 11,
    "supplier_id": 34,
    "supplier_code": "SUP423",
    "supplier_part_number": "E-86805-uTM"
    }

    try:
        # Send a PUT request to update the specific item
        response = requests.put(url, json=updated_payload, headers={'API_KEY': API_KEY})

        # Verify that the status code is 400 (Bad Request)
        assert response.status_code == 400

        if response.status_code == 200:
            response_data = response.json()
            print(f"Item successfully updated: {response_data}")
        elif response.status_code == 404:
            print("Item not found, cannot update")
        else:
            print("Server error when trying to update item")
    
    # Catch any requests-related errors, including timeouts
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")



#this test should return an 403 if you dont have an extra key
#because not everyone that has acces to the API should have 
# the option to delete an item
# so in the delete request there needs to be like an second admin API key
def test_delete_itemss(_url):
    url = _url + 'items'
    params = {'uid': 'p6942069'}

    # Send a DELETE request to delete a item by ID
    response = requests.delete(url, params=params, headers={'API_KEY': API_KEY})

    # Verify that the status code is 403 (forbidden)
    assert response.status_code == 403



if __name__ == "__main__":
    pytest.main()
