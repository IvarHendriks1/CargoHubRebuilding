import pytest
import requests


@pytest.fixture
def _url():
    return 'http://localhost:3000/api/v1/'


headers = {
            'Accept': '/',
            'User-Agent': 'value',
            'API_KEY': 'a1b2c3d4e5' #  the API key
        }


def test_get_all_warehouses(_url):
    url = _url + 'warehouses'

    # Send a GET request to the API
    response = requests.get(url,headers=headers)

    # Get the status code and response data
    status_code = response.status_code
    response_data = response.json()

    # Verify that the status code is 200 (OK)
    assert status_code == 200

    # Verify the response data

#---------------------------------------------------------------------------------------------------------------------

def test_post_warehouse_by_id(_url):
    url = _url + 'warehouses/9999999'
    #params = {"id": 9999999}

    body = {
        "id": 9999999,
        "code": "QAQMNLCL",
        "name": "testing warehouse, should be deleted after test",
        "address": "Noaboulevard 7",
        "zip": "1735XO",
        "city": "Hoogeveen",
        "province": "Zuid-Holland",
        "country": "NL",
        "contact": {
            "name": "Sjoerd Sterkman",
            "phone": "0943-736616",
            "email": "imkehermans@example.org"
        },
        "created_at": "2017-11-03 19:21:26",
        "updated_at": "2023-05-30 16:45:10"
    }

    # POST the testing warehouse
    posting = requests.post(url, json=body, headers=headers)

    # Get the status code and response data
    post_status_code = posting.status_code

    # Verify that the status code is 200 (OK)
    assert post_status_code == 201

#---------------------------------------------------------------------------------------------------------------------

def test_get_warehouse_by_id(_url):
    url = _url + 'warehouses/9999999'
    # Send a GET request to the API
    response = requests.get(url,headers=headers)

    # Get the status code and response data
    get_status_code = response.status_code
    response_data = response.json()

    # Verify that the status code is 200 (OK)
    assert get_status_code == 200

    # Verify the response data
    assert response_data['id'] == 9999999
    assert response_data['code'] == 'QAQMNLCL'
    assert response_data['name'] == 'testing warehouse, should be deleted after test'
    assert response_data['address'] == 'Noaboulevard 7'
    assert response_data['zip'] == '1735XO'
    assert response_data['city'] == 'Hoogeveen'
    assert response_data['province'] == 'Zuid-Holland'
    assert response_data['country'] == 'NL'
    assert response_data["contact"]['name'] == 'Sjoerd Sterkman'
    assert response_data["contact"]['phone'] == '0943-736616'
    assert response_data["contact"]['email'] == 'imkehermans@example.org'

#---------------------------------------------------------------------------------------------------------------------
    
def test_put_warehouse_by_id(_url):
    url = _url + 'warehouses/9999999'
    response = requests.get(url,headers=headers)

    # Get the status code and response data
    get_status_code = response.status_code
    response_data = response.json()

    # Verify that the status code is 200 (OK)
    assert get_status_code == 200

    # Verify the response data
    assert response_data['id'] == 9999999
    assert response_data['code'] == 'QAQMNLCL'

    body = {
        "id": 9999999,
        "code": "ABCDEFGH",
        "name": "NEW testing warehouse, this has been changed",
        "address": "testing boulevard 8",
        "zip": "8723FG",
        "city": "Rotterdam",
        "province": "Noord-Holland",
        "country": "BE",
        "contact": {
            "name": "John Doe",
            "phone": "1234-56789",
            "email": "testing@mail.com"
        },
        "created_at": "2017-11-03 19:21:26",
        "updated_at": "2023-05-30 16:45:10"
    }
    
    response = requests.put(url,json=body,headers=headers)
    

    # Verify that the status code is 200 (OK)
    assert get_status_code == 200

    response = requests.get(url,headers=headers)

    # Get the status code and response data
    get_status_code = response.status_code
    response_data = response.json()

    # Verify that the status code is 200 (OK)
    assert get_status_code == 200

    # Verify the response data
    assert response_data['id'] == 9999999
    assert response_data['code'] == 'ABCDEFGH'
    assert response_data['name'] == 'NEW testing warehouse, this has been changed'
    assert response_data['address'] == 'testing boulevard 8'
    assert response_data['zip'] == '8723FG'
    assert response_data['city'] == 'Rotterdam'
    assert response_data['province'] == 'Noord-Holland'
    assert response_data['country'] == 'BE'
    assert response_data["contact"]['name'] == 'John Doe'
    assert response_data["contact"]['phone'] == '1234-56789'
    assert response_data["contact"]['email'] == 'testing@mail.com'
    
#---------------------------------------------------------------------------------------------------------------------

def test_delete_warehouse(_url):
    url = _url + "warehouses/9999999"

    response = requests.delete(url,headers=headers)
    delete_status_code = response.status_code
    #response_data = response.json()
    assert delete_status_code == 200
    #assert response_data == []
    
    response = requests.get(url,headers=headers)
    
    # Get the status code and response data
    get_status_code = response.status_code
    response_data = response.json()

    # Verify that the status code is 200 (OK)
    assert get_status_code == 200

    # Verify the response data
    assert response_data == None

#---------------------------------------------------------------------------------------------------------------------


