from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_user_by_id():
    response = client.get("/users/1")
    assert response.status_code == 200 or response.status_code == 404

def test_create_user():
    user_data = {"name": "John Doe", "email": "john.doe@example.com", "password": "password123"}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

def test_update_user():
    user_data = {"name": "John Doe Updated", "email": "john.doe.updated@example.com"}
    response = client.put("/users/1", json=user_data)
    assert response.status_code == 200 or response.status_code == 404

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200 or response.status_code == 404
