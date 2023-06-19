from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .services import StoreService
from core.database import get_db_session
from .schema import Store

router = APIRouter()


@router.get("/", response_model=List[Store])
def get(db: Session = Depends(get_db_session)):
    store = StoreService(db).get_store_all()
    return store


@router.get("/{id}", response_model=Store)
def get(id: int, db: Session = Depends(get_db_session)):
    store = StoreService(db).get_store_one(id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store


@router.post("/", response_model=Store)
def post(store: Store, db: Session = Depends(get_db_session)):
    return StoreService(db).store_create(store)


@router.put("/{id}", response_model=Store)
def put(id: int, store: Store, db: Session = Depends(get_db_session)):
    store = StoreService(db).store_update(id, store)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store


@router.delete("/{id}", response_model=Store)
def delete(id: int, db: Session = Depends(get_db_session)):
    store = StoreService(db).store_delete(id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store
