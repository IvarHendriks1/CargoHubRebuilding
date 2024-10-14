import pytest
import requests
import datetime


@pytest.fixture
def _url():
    return 'http://localhost:3000/api/v1/'


headers = {
            'Accept': '/',
            'User-Agent': 'value',
            'API_KEY': 'a1b2c3d4e5' 
        }

def test_get_all_locations(_url):
    url = _url + 'locations'

    # Send a GET request to the API
    response = requests.get(url,headers=headers)

    # Get the status code and response data
    status_code = response.status_code
    response_data = response.json()

    assert status_code == 200

    # Ensure the response is a list (assuming it returns multiple locations)
    assert isinstance(response_data, list)

    # Check that each location entry in the response has the required keys
    for location in response_data:
        assert isinstance(location, dict)
    
        # check the fields
        assert 'id' in location
        assert 'warehouse_id' in location
        assert 'code' in location
        assert 'name' in location
        assert 'created_at' in location
        assert 'updated_at' in location

        # check the data types 
        assert isinstance(location['id'], int)
        assert isinstance(location['warehouse_id'], int)
        assert isinstance(location['code'], str)
        assert isinstance(location['name'], str)
        assert isinstance(location['created_at'], str)
        assert isinstance(location['updated_at'], str)

#---------------------------------------------------------------------------------------------------------------------

def test_post_location(_url):
    url = _url + 'locations'

    body = {
        "id": 999999999,
        "warehouse_id": 999999999,
        "code": "Z.9.1",
        "name": "Row: Z, Rack: 9, Shelf: 1",
        "created_at": "2024-10-13 03:21:32",
        "updated_at": "2024-10-13 03:21:32"
    }

    # Send a POST request to the API
    response = requests.post(url,json=body,headers=headers)

    # Get the status code 
    status_code = response.status_code
    assert status_code == 201

    # Send a GET request to the API
    response = requests.get(url+"/999999999",headers=headers)

    # Get the status code and response data
    status_code = response.status_code
    response_data = response.json()

    assert status_code == 200

    # Check if the response is a dictionary
    assert isinstance(response_data, dict)

    # check the fields
    assert "id" in response_data
    assert "warehouse_id" in response_data
    assert "code" in response_data
    assert "name" in response_data
    assert "created_at" in response_data
    assert "updated_at" in response_data

    # check the data types 
    assert isinstance(response_data["id"], int)
    assert isinstance(response_data["warehouse_id"], int)
    assert isinstance(response_data["code"], str)
    assert isinstance(response_data["name"], str)
    assert isinstance(response_data["created_at"], str)
    assert isinstance(response_data["updated_at"], str)

    # check the data itself
    assert response_data["id"] == 999999999
    assert response_data["warehouse_id"] == 999999999
    assert response_data["code"] == "Z.9.1"
    assert response_data["name"] == "Row: Z, Rack: 9, Shelf: 1"

#--------------------------------------------------------------------------------------------------------------------- 

def test_put_location(_url):
    url = _url + 'locations/999999999'
    
    # Send a GET request to the API
    response = requests.get(url,headers=headers)

    # Get the status code and response data
    status_code = response.status_code
    response_data = response.json()

    assert status_code == 200

    # Check if the response is a dictionary
    assert isinstance(response_data, dict)

    # check the fields
    assert "id" in response_data
    assert "warehouse_id" in response_data
    assert "code" in response_data
    assert "name" in response_data
    assert "created_at" in response_data
    assert "updated_at" in response_data

    # check the data types 
    assert isinstance(response_data["id"], int)
    assert isinstance(response_data["warehouse_id"], int)
    assert isinstance(response_data["code"], str)
    assert isinstance(response_data["name"], str)
    assert isinstance(response_data["created_at"], str)
    assert isinstance(response_data["updated_at"], str)

    # check the data itself
    assert response_data["id"] == 999999999
    assert response_data["warehouse_id"] == 999999999
    assert response_data["code"] == "Z.9.1"
    assert response_data["name"] == "Row: Z, Rack: 9, Shelf: 1"

    # made chenges to the body of the test location  
    body = {
        "id": 999999999,
        "warehouse_id": 999999888,
        "code": "X.6.6",
        "name": "Row: X, Rack: 6, Shelf: 6",
        "created_at": "2024-10-13 03:21:32",
        "updated_at": "2024-10-13 03:21:32"
    }

    # Send a PUT request to the API with the changed body
    response = requests.put(url,json=body,headers=headers)

    # Get the status code
    status_code = response.status_code
    assert status_code == 200

    # Send a GET request to the API
    response = requests.get(url,headers=headers)

    # Get the status code and response data
    status_code = response.status_code
    response_data = response.json()

    assert status_code == 200

    # Check that each location entry in the response has the required keys
    
    assert isinstance(response_data, dict)

    # check the fields
    assert "id" in response_data
    assert "warehouse_id" in response_data
    assert "code" in response_data
    assert "name" in response_data
    assert "created_at" in response_data
    assert "updated_at" in response_data

    # check the data types 
    assert isinstance(response_data["id"], int)
    assert isinstance(response_data["warehouse_id"], int)
    assert isinstance(response_data["code"], str)
    assert isinstance(response_data["name"], str)
    assert isinstance(response_data["created_at"], str)
    assert isinstance(response_data["updated_at"], str)

    # check the data itself
    assert response_data["id"] == 999999999
    assert response_data["warehouse_id"] == 999999888
    assert response_data["code"] == "X.6.6"
    assert response_data["name"] == "Row: X, Rack: 6, Shelf: 6"


#--------------------------------------------------------------------------------------------------------------------- 

def test_delete_location(_url):
    url = _url + 'locations/999999999'

    # Send a GET request to the API
    response = requests.delete(url,headers=headers)

    # Get the status code and response data
    status_code = response.status_code

    assert status_code == 200

     # Send a GET request to the API
    response = requests.get(url,headers=headers)

    # Get the status code and response data
    status_code = response.status_code
    response_data = response.text

    assert status_code == 200
    assert response_data == "null"

#---------------------------------------------------------------------------------------------------------------------
