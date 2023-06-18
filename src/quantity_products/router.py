from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from typing import List

from .service import QuantityProductsService
from core.database import get_db_session
from .schema import QuantityProducts

router = APIRouter()


@router.get("/", response_model=List[QuantityProducts])
def read_devices(db: Session = Depends(get_db_session)):
    quantity_products = QuantityProducts(db).get_quantity_product_all()
    return quantity_products


@router.get("/{id}", response_model=QuantityProducts)
def read_device(id: int, db: Session = Depends(get_db_session)):
    quantity_product = QuantityProductsService(db).get_quantity_product_one(id)
    if not quantity_product:
        raise HTTPException(status_code=404, detail="QuantityProducts not found")
    return quantity_product


@router.post("/", response_model=QuantityProducts)
def create_device(device: QuantityProducts, db: Session = Depends(get_db_session)):
    return QuantityProductsService(db).get_quantity_product_create(device)


@router.put("/{id}", response_model=QuantityProducts)
def update_device(id: int, device: QuantityProducts, db: Session = Depends(get_db_session)):
    updated_device = QuantityProductsService(db).get_quantity_product_update(id, device)
    if not updated_device:
        raise HTTPException(status_code=404, detail="QuantityProducts not found")
    return updated_device


@router.delete("/{id}", response_model=QuantityProducts)
def delete_device(id: int, db: Session = Depends(get_db_session)):
    deleted_device = QuantityProductsService(db).get_quantity_product_delete(id)
    if not deleted_device:
        raise HTTPException(status_code=404, detail="QuantityProducts not found")
    return deleted_device
