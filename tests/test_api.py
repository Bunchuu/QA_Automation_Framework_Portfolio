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
