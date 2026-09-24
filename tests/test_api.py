import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


def test_get_single_post():
    response = requests.get(f"{BASE_URL}/1")
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == 1
    assert data["userId"] == 1


def test_create_post():
    payload = {
        "title": "Portfolio Automation",
        "body": "Continuous Integration Test",
        "UserId": 1
    }
    response = requests.post(BASE_URL, json=payload)
    data = response.json()

    assert response.status_code == 201
    assert data["title"] == payload["title"]
    assert "id" in data


def test_update_post_success():
    payload = {
        "title": "Updated Title",
        "body": "Updated Body",
        "userId": 1,
        "id": 1
    }
    response = requests.put(f"{BASE_URL}/1", json=payload)
    data = response.json()

    assert response.status_code == 200
    for key in payload.keys():
        assert data[key] == payload[key]


def test_delete_post_success():
    response = requests.delete(f"{BASE_URL}/1")
    data = response.json()

    assert response.status_code in [200, 204]
    assert data == {}


def test_get_non_existent_post_returns_404():
    response = requests.get(f"{BASE_URL}/9999")

    assert response.status_code == 404