from fastapi.testclient import TestClient


def test_register(test_client: TestClient):

    response = test_client.post(
        "/auth/register",
        json={
            "username": "admin",
            "email": "admin@gmail.com",
            "password": "admin123",
            "role": "Admin"
        }
    )

    assert response.status_code in [200, 400]


def test_login(test_client: TestClient):

    response = test_client.post(
        "/auth/login",
        data={
            "username": "admin@gmail.com",
            "password": "admin123"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()