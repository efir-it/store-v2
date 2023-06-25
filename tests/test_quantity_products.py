# from fastapi.testclient import TestClient
# import pytest
#
# from main import app
#
# client = TestClient(app)
#
#
# def test_get_all_quantity_products(client):
#     response = client.get("/quantity_products/")
#     assert response.status_code == 200
#     assert len(response.json()) >= 0
#
#
# def test_get_one_quantity_product(client):
#     response = client.get(f"/quantity_products/{id}")
#     assert response.status_code == 200
#     assert response.json()["id"] == id
#
#
# def test_create_quantity_product(client):
#     data = {"product": "test product", "store_id": 1, "count": 10}
#     response = client.post("/quantity_products/", json=data)
#     assert response.status_code == 200
#     assert response.json()["product"] == data["product"]
#     assert response.json()["store_id"] == data["store_id"]
#     assert response.json()["count"] == data["count"]
#
#
# def test_update_quantity_product(client):
#     data = {"product": "updated product", "store_id": 1, "count": 15}
#     response = client.put(f"/quantity_products/{id}", json=data)
#     assert response.status_code == 200
#     assert response.json()["product"] == data["product"]
#     assert response.json()["store_id"] == data["store_id"]
#     assert response.json()["count"] == data["count"]
#
#
# def test_delete_quantity_product(client):
#     response = client.delete(f"/quantity_products/{id}")
#     assert response.status_code == 200
#     assert response.json()["id"] == id
#
#
# def test_get_nonexisting_quantity_product(client):
#     response = client.get("/quantity_products/999")
#     assert response.status_code == 404
#     assert response.json()["detail"] == "QuantityProducts not found"
