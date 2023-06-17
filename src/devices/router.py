from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .services import DevicesService
from core.database import get_db_session
from .schema import Devices, DevicesCreate, DevicesUpdate

router = APIRouter()


@router.get("/devices", response_model=List[Devices])
def read_devices(db: Session = Depends(get_db_session)):
    devices = DevicesService(db).get_devices()
    return devices


@router.get("/{id}", response_model=Devices)
def read_device(id: int, db: Session = Depends(get_db_session)):
    device = DevicesService(db).get_device(id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device


@router.post("/", response_model=Devices)
def create_device(device: DevicesCreate, db: Session = Depends(get_db_session)):
    return DevicesService(db).create_device(device)


@router.put("/{id}", response_model=Devices)
def update_device(id: int, device: DevicesUpdate, db: Session = Depends(get_db_session)):
    updated_device = DevicesService(db).update_device(id, device)
    if not updated_device:
        raise HTTPException(status_code=404, detail="Device not found")
    return updated_device


@router.delete("/{id}", response_model=Devices)
def delete_device(id: int, db: Session = Depends(get_db_session)):
    deleted_device = DevicesService(db).delete_device(id)
    if not deleted_device:
        raise HTTPException(status_code=404, detail="Device not found")
    return deleted_device
