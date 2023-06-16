from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.database import get_db_session
from src.type_device.services import TypeDeviceService


router = APIRouter()


@router.get("/{type_device_id}")
def get_type_device(type_device_id: int, db_session: Session = Depends(get_db_session)):
    service = TypeDeviceService(db_session)
    type_device = service.get_type_device(type_device_id)
    if not type_device:
        raise HTTPException(status_code=404, detail="Type device not found")
    return type_device


@router.get("/")
def get_all_type_devices(db_session: Session = Depends(get_db_session)):
    service = TypeDeviceService(db_session)
    type_devices = service.get_all_type_devices()
    return type_devices


@router.post("/")
def create_type_device(name: str, db_session: Session = Depends(get_db_session)):
    service = TypeDeviceService(db_session)
    type_device = service.create_type_device(name)
    return type_device


@router.put("/{type_device_id}")
def update_type_device(type_device_id: int, name: str, db_session: Session = Depends(get_db_session)):
    service = TypeDeviceService(db_session)
    type_device = service.update_type_device(type_device_id, name)
    if not type_device:
        raise HTTPException(status_code=404, detail="Type device not found")
    return type_device


@router.delete("/{type_device_id}")
def delete_type_device(type_device_id: int, db_session: Session = Depends(get_db_session)):
    service = TypeDeviceService(db_session)
    type_device = service.get_type_device(type_device_id)
    if not type_device:
        raise HTTPException(status_code=404, detail="Type device not found")
    service.delete_type_device(type_device_id)
    return {"message": "Type device deleted successfully"}
