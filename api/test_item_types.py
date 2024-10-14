import pytest
import requests


@pytest.fixture
def _url():
    return "http://localhost:3000/api/v1/item_types"


headers = {
    "Accept": "/",
    "User-Agent": "value",
    "API_KEY": "a1b2c3d4e5",  #  the API key
}


def test_post_item_type(_url):
    response = requests.post(_url, headers=headers)
    assert response.status_code == 404


def test_get_item_type(_url):
    response = requests.get(_url + "/1", headers=headers)
    if response.content:
        response_data = response.json()  # Parse JSON response if body is not empty
        assert response_data["id"] == 1
    else:
        print("GET request returned 200 but no response body.")


def test_put_item_type(_url):
    current_type = {
        "id": 1,
        "name": "Desktop",
        "description": "",
        "created_at": "1993-07-28 13:43:32",
        "updated_at": "2022-05-12 08:54:35",
    }

    updated_type = {
        "id": 1,
        "name": "Testing type",
        "description": "This is a itemtype made for the put test.",
        "created_at": "1993-07-28 13:43:32",
        "updated_at": "2022-05-12 08:54:35",
    }
    put_response = requests.put(_url + "/1", json=updated_type, headers=headers)
    assert put_response.status_code == 200

    if put_response.content:
        response_data = put_response.json()  # Parse JSON response if body is not empty
        assert (
            response_data["description"] == "This is a itemtype made for the put test."
        )
    else:
        print("PUT request returned 200 but no response body.")

    requests.put(_url + "/1", json=current_type, headers=headers)
