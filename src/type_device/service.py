from model import TypeDevice as TypeDeviceModel
from schema import TypeDevice as TypeDeviceSchema
from sqlalchemy.orm import Session


def create_type_device(data: TypeDeviceSchema.TypeDeviceModel, db: Session):
    type_device = TypeDeviceModel(name=data.name)
    try:
        db.add(type_device)
        db.commit()
        db.refresh(type_device)
    except Exception as e:
        print(e)
    return type_device


def get_type_device(type_device_id: int):
    pass


def get_type_device_list():
    pass


def update_type_device(session):
    type_device = ''
    await session.execute(type_device)
    await session.commit()
    return {"status": "success"}


def delete_type_device(session):
    ...
