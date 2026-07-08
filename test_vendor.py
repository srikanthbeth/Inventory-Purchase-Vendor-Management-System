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


def test_create_vendor(test_client: TestClient):

    token = get_token(test_client)

    response = test_client.post(
        "/vendors/",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "vendor_name": "ABC Traders",
            "email": "abc@gmail.com",
            "phone": "9876543210",
            "address": "Hyderabad"
        }
    )

    assert response.status_code in [200, 400]


def test_get_all_vendors(test_client: TestClient):

    token = get_token(test_client)

    response = test_client.get(
        "/vendors/",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200


def test_get_vendor_by_id(test_client: TestClient):

    token = get_token(test_client)

    response = test_client.get(
        "/vendors/1",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code in [200, 404]


def test_update_vendor(test_client: TestClient):

    token = get_token(test_client)

    response = test_client.put(
        "/vendors/1",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "phone": "9999999999"
        }
    )

    assert response.status_code in [200, 404]


def test_delete_vendor(test_client: TestClient):

    token = get_token(test_client)

    response = test_client.delete(
        "/vendors/1",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code in [200, 404]