def test():
    assert 1 == 1


from fastapi.testclient import TestClient
import pytest

from main import app

client = TestClient(app)
#
#
# @pytest.fixture(scope="module")
# def test_db():
#     # здесь может быть логика создания и удаления тестовой базы данных
#     yield
#     # здесь может быть логика удаления тестовых данных из базы данных
#
#
def test_create_store(test_db):
    response = client.post("/store/", json={"name": "TestStore", "address": "TestAddress", "separated": True})
    assert response.status_code == 200
    assert response.json()["name"] == "TestStore"
#
#
# def test_get_stores(test_db):
#     client.post("/store/", json={"name": "TestStore1", "address": "TestAddress1", "separated": True})
#     client.post("/store/", json={"name": "TestStore2", "address": "TestAddress2", "separated": False})
#
#     response = client.get("/store/")
#     assert response.status_code == 200
#     assert len(response.json()) == 2
#
#
# def test_get_store(test_db):
#     store_id = client.post("/store/", json={"name": "TestStore3", "address": "TestAddress3", "separated": True}).json()[
#         "id"]
#     response = client.get(f"/store/{store_id}")
#     assert response.status_code == 200
#     assert response.json()["name"] == "TestStore3"
#
#
# def test_update_store(test_db):
#     store_id = client.post("/store/", json={"name": "TestStore4", "address": "TestAddress4", "separated": True}).json()[
#         "id"]
#     response = client.put(f"/store/{store_id}", json={"name": "NewName", "address": "NewAddress"})
#     assert response.status_code == 200
#     assert response.json()["name"] == "NewName"
#
#
# def test_delete_store(test_db):
#     store_id = client.post("/store/", json={"name": "TestStore5", "address": "TestAddress5", "separated": True}).json()[
#         "id"]
#     response = client.delete(f"/store/{store_id}")
#     assert response.status_code == 200
#     assert response.json()["name"] == "TestStore5"