from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .services import StoreService
from core.database import get_db_session
from .schema import Store

router = APIRouter()


@router.get("/", response_model=List[Store])
def read_devices(db: Session = Depends(get_db_session)):
    devices = StoreService(db).get_store_all()
    return devices


@router.get("/{id}", response_model=Store)
def read_device(id: int, db: Session = Depends(get_db_session)):
    device = StoreService(db).get_store_one(id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device


@router.post("/", response_model=Store)
def create_device(device: Store, db: Session = Depends(get_db_session)):
    return StoreService(db).get_store_create(device)


@router.put("/{id}", response_model=Store)
def update_device(id: int, store: Store, db: Session = Depends(get_db_session)):
    store = StoreService(db).get_store_update(id, store)
    if not store:
        raise HTTPException(status_code=404, detail="Device not found")
    return store


@router.delete("/{id}", response_model=Store)
def delete_device(id: int, db: Session = Depends(get_db_session)):
    store = StoreService(db).get_store_delete(id)
    if not store:
        raise HTTPException(status_code=404, detail="Device not found")
    return store
