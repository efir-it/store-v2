
from unittest.mock import MagicMock
import sqlite3
import pytest


from ..src.quantity_products.model import QuantityProducts
from ..src.quantity_products.service import QuantityProductsService
from ..src.store.model import Store
from ..src.store.services import StoreService
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:542525Zz@localhost:5432/store_test"
SQLALCHEMY_DATABASE_URL = "sqlite:///test.db"

engine_test = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test, extend_existing=True)



def get_db_test_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def store():
    service = StoreService

    store_1 = Store(id=1, name='Магазин Бавария', address="Ворошилова 32", separated=True)
    store_2 = Store(id=2, name='Магазин Бавария', address="Конституции 1/1", separated=True)
    store_3 = Store(id=3, name='Магазин Бавария', address="Победы 159", separated=True)

    service.get_store_one = MagicMock(return_value=store_1)
    service.get_store_all = MagicMock(return_value=[store_1, store_2, store_3])
    service.store_update = MagicMock(return_value={"updated_rows": 1, "id": "2", "answer": "updated"})
    service.store_create = MagicMock(return_value=store_2)
    service.store_delete = MagicMock(return_value={'answer': 'success'})

    return service


@pytest.fixture
def store():
    service = QuantityProductsService

    quantity_product_1 = QuantityProducts(id=1, product="Темное пиво", store_id=1, count=5)
    quantity_product_2 = QuantityProducts(id=2, product="Светлое пиво", store_id=1, count=15)
    quantity_product_3 = QuantityProducts(id=3, product="Чипсы", store_id=1, count=50)

    service.get_quantity_product_one = MagicMock(return_value=quantity_product_1)
    service.get_quantity_product_all = MagicMock(return_value=[quantity_product_1, quantity_product_2, quantity_product_3])
    service.quantity_product_update = MagicMock(return_value={"updated_rows": 1, "id": "2", "answer": "updated"})
    service.quantity_product_create = MagicMock(return_value=quantity_product_2)
    service.quantity_product_delete = MagicMock(return_value={'answer': 'success'})

    return service
