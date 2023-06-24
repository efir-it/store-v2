from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from typing import List

from .service import QuantityProductsService
from core.database import get_db_session
from .schema import QuantityProducts

router = APIRouter()


@router.get("/", response_model=List[QuantityProducts])
def get(db: Session = Depends(get_db_session)):
    quantity_products = QuantityProductsService(db).get_quantity_product_all()
    return quantity_products


@router.get("/{id}", response_model=QuantityProducts)
def get(id: int, db: Session = Depends(get_db_session)):
    quantity_product = QuantityProductsService(db).get_quantity_product_one(id)
    if not quantity_product:
        raise HTTPException(status_code=404, detail="QuantityProducts not found")
    return quantity_product


@router.post("/", response_model=QuantityProducts)
def post(device: QuantityProducts, db: Session = Depends(get_db_session)):
    return QuantityProductsService(db).quantity_product_create(device)


@router.put("/{id}", response_model=QuantityProducts)
def put(id: int, quantity_product: QuantityProducts, db: Session = Depends(get_db_session)):
    quantity_product = QuantityProductsService(db).quantity_product_update(id, quantity_product)
    if not quantity_product:
        raise HTTPException(status_code=404, detail="QuantityProducts not found")
    return quantity_product


@router.delete("/{id}", response_model=QuantityProducts)
def delete(id: int, db: Session = Depends(get_db_session)):
    quantity_product = QuantityProductsService(db).quantity_product_delete(id)
    if not quantity_product:
        raise HTTPException(status_code=404, detail="QuantityProducts not found")
    return quantity_product
