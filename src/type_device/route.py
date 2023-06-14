from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import service as TypeDeviceServices
from model import TypeDevice as TypeDeviceModel

router = APIRouter()


@router.get("/type_device/{id}")
def get_type_device(type_device_id: int):
    pass


@router.get("")
def get_type_device_list():
    pass


@router.post('/', tags=['create_type_device'])
def create_type_device(data, db: Session):
    return TypeDeviceServices.create_type_device(data, db)


