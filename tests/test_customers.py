from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_customers():
    response = client.get("/customers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_customer_by_id():
    response = client.get("/customers/1")
    assert response.status_code == 200 or response.status_code == 404

def test_create_customer():
    new_customer = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "1234567890",
        "address": "123 Main St"
    }
    response = client.post("/customers/", json=new_customer)
    assert response.status_code == 200
    assert response.json()["name"] == new_customer["name"]

def test_update_customer():
    updated_customer = {
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "phone": "0987654321",
        "address": "456 Main St"
    }
    response = client.put("/customers/1", json=updated_customer)
    assert response.status_code == 200 or response.status_code == 404

def test_delete_customer():
    response = client.delete("/customers/1")
    assert response.status_code == 200 or response.status_code == 404
