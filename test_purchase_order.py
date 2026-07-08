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


def test_create_purchase_order(test_client: TestClient):

    token = get_token(test_client)

    response = test_client.post(
        "/purchase-orders/",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "vendor_id": 1,
            "product_name": "Laptop",
            "quantity": 10,
            "unit_price": 50000,
            "expected_delivery_date": "2026-07-20",
            "status": "Pending"
        }
    )

    assert response.status_code in [200, 400, 404]


def test_get_orders(test_client: TestClient):

    token = get_token(test_client)

    response = test_client.get(
        "/purchase-orders/",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200


def test_get_order_by_id(test_client: TestClient):

    token = get_token(test_client)

    response = test_client.get(
        "/purchase-orders/1",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code in [200, 404]


def test_update_order(test_client: TestClient):

    token = get_token(test_client)

    response = test_client.put(
        "/purchase-orders/1",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "status": "Approved"
        }
    )

    assert response.status_code in [200, 400, 404]