from sqlalchemy.orm import Session

from . import model, schema


class DriversService:
    def __init__(self, db: Session):
        self.db = db

    def get_driver_one(self, driver_id: int):
        return self.db.query(model.Driver).filter(model.Driver.id == driver_id).first()

    def get_driver_all(self):
        return self.db.query(model.Driver).all()

    def driver_create(self, data: schema.Drivers):
        quantity_product = model.Driver(name=data.name, position_save=data.position_save, model_device=data.model_device)
        self.db.add(quantity_product)
        self.db.commit()
        self.db.refresh(quantity_product)
        return quantity_product

    def driver_update(self, driver_id: int, data: schema.Drivers):
        driver = self.get_driver_one(driver_id)
        if not driver:
            return None

        for key, value in data.items():
            setattr(driver, key, value)

        self.db.commit()
        self.db.refresh(driver)
        return driver

    def driver_delete(self, product_id: int):
        driver = self.get_driver_one(product_id)

        if not driver:
            return None

        self.db.delete(driver)
        self.db.commit()
        return driver
