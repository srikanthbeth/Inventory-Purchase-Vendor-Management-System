from fastapi.testclient import TestClient


def get_token(client: TestClient):

    response = client.post(
        "/auth/login",
        data={
            "username": "admin@gmail.com",
            "password": "admin123"
        }
    )

    return response.json()["access_token"]


def test_purchase_history(test_client: TestClient):

    token = get_token(test_client)

    response = test_client.get(
        "/reports/vendor/1",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200


def test_filter_status(test_client: TestClient):

    token = get_token(test_client)

    response = test_client.get(
        "/reports/status/Pending",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200


def test_search_product(test_client: TestClient):

    token = get_token(test_client)

    response = test_client.get(
        "/reports/search/?product_name=Laptop",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200


def test_pagination(test_client: TestClient):

    token = get_token(test_client)

    response = test_client.get(
        "/reports/pagination/?page=1&limit=5",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200