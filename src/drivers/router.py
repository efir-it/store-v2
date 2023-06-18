from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .services import DriversService
from core.database import get_db_session
from .schema import Drivers

router = APIRouter()


@router.get("/", response_model=List[Drivers])
def get_devices(db: Session = Depends(get_db_session)):
    driver = DriversService(db).get_driver_all()
    return driver


@router.get("/{id}", response_model=Drivers)
def get_device(id: int, db: Session = Depends(get_db_session)):
    driver = DriversService(db).get_driver_one(id)
    if not driver:
        raise HTTPException(status_code=404, detail="Device not found")
    return driver


@router.post("/", response_model=Drivers)
def create_device(driver: Drivers, db: Session = Depends(get_db_session)):
    return DriversService(db).driver_create(driver)


@router.put("/{id}", response_model=Drivers)
def update_device(id: int, driver: Drivers, db: Session = Depends(get_db_session)):
    driver = DriversService(db).driver_update(id, driver)
    if not driver:
        raise HTTPException(status_code=404, detail="Device not found")
    return driver


@router.delete("/{id}", response_model=Drivers)
def delete_device(id: int, db: Session = Depends(get_db_session)):
    driver = DriversService(db).driver_delete(id)
    if not driver:
        raise HTTPException(status_code=404, detail="driver not found")
    return driver
