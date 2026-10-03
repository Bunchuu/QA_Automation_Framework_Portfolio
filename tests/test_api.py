import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


@pytest.mark.parametrize("post_id, expected_user_id",[
    (1, 1),
    (2, 1),
    (3, 1)
])
def test_get_single_post(post_id, expected_user_id):
    response = requests.get(f"{BASE_URL}/{post_id}")
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == post_id
    assert data["userId"] == expected_user_id


@pytest.mark.parametrize("payload", [
    {"title": "Portfolio Automation",
    "body": "Continuous Integration Test",
    "UserId": 1},
    {"title": "X",
     "body": "abc",
     "UserId": 7},
     {"title": "Y",
      "body": "def",
      "UserId": 15}
])
def test_create_post(payload):
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
    for key, value in payload.items():
        assert data[key] == value


def test_delete_post_success():
    response = requests.delete(f"{BASE_URL}/1")
    data = response.json()

    assert response.status_code in [200, 204]
    assert data == {}


@pytest.mark.parametrize("post_id", [-1, 0, 99999])
def test_get_non_existent_post_returns_404(post_id):
    response = requests.get(f"{BASE_URL}/{post_id}")

    assert response.status_code == 404


def test_get_all_posts_returns_list():
    response = requests.get(BASE_URL)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0