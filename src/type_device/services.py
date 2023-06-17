from sqlalchemy.orm import Session

from . import model, schema


class TypeDeviceService:
    def __init__(self, db: Session):
        self.db = db

    def get_type_device(self, type_device_id: int):
        return self.db.query(model.TypeDevice).filter(model.TypeDevice.id == type_device_id).first()

    def get_all_type_devices(self, skip: int = 0, limit: int = 100):
        return self.db.query(model.TypeDevice).offset(skip).limit(limit).all()

    def create_type_device(self, type_device):
        db_type_device = model.TypeDevice(name=type_device)
        self.db.add(db_type_device)
        self.db.commit()
        self.db.refresh(db_type_device)
        return db_type_device

    def update_type_device(self, type_device_id: int, type_device: schema.TypeDeviceUpdate):
        db_type_device = self.db.query(model.TypeDevice).filter(model.TypeDevice.id == type_device_id).first()
        if db_type_device:
            db_type_device.name = type_device
            self.db.commit()
            self.db.refresh(db_type_device)
            return db_type_device

    def delete_type_device(self, type_device_id: int):
        db_type_device = self.db.query(model.TypeDevice).filter(model.TypeDevice.id == type_device_id).first()
        if db_type_device:
            self.db.delete(db_type_device)
            self.db.commit()
            return db_type_device
