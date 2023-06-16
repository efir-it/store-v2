from sqlalchemy.orm import Session

from . import model, schema


class DevicesService:
    def __init__(self, db: Session):
        self.db = db

    def get_device(self, device_id: int):
        return self.db.query(model.Devices).filter(model.Devices.id == device_id).first()

    def get_devices(self, skip: int = 0, limit: int = 100):
        return self.db.query(model.Devices).offset(skip).limit(limit).all()

    def create_device(self, device: schema.DevicesCreate):
        db_device = model.Devices(name=device.name, hide=device.hide,
                                   rmk_id=device.rmk_id, type_device_id=device.type_device_id)
        self.db.add(db_device)
        self.db.commit()
        self.db.refresh(db_device)
        return db_device

    def update_device(self, device_id: int, device: schema.DevicesUpdate):
        db_device = self.get_device(device_id)
        if not db_device:
            return None
        for key, value in device.dict(exclude_unset=True).items():
            setattr(db_device, key, value)
        self.db.commit()
        self.db.refresh(db_device)
        return db_device

    def delete_device(self, device_id: int):
        db_device = self.get_device(device_id)
        if not db_device:
            return None
        self.db.delete(db_device)
        self.db.commit()
        return db_device