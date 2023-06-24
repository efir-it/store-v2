from sqlalchemy.orm import Session

from . import model, schema


class QuantityProductsService:
    def __init__(self, db: Session):
        self.db = db

    def get_quantity_product_one(self, id: int):
        return self.db.query(model.QuantityProducts).filter(model.QuantityProducts.id == id).first()

    def get_quantity_product_all(self):
        return self.db.query(model.QuantityProducts).all()

    def quantity_product_create(self, data: schema.QuantityProducts):
        quantity_product = model.QuantityProducts(product=data.product, store_id=data.store_id, count=data.count)
        self.db.add(quantity_product)
        self.db.commit()
        self.db.refresh(quantity_product)
        return quantity_product

    def quantity_product_update(self, product_id: int, data: schema.QuantityProducts):
        quantity_product = self.get_quantity_product_one(product_id)
        if not quantity_product:
            return None

        for key, value in data.__dict__.items():
            setattr(quantity_product, key, value)

        self.db.commit()
        self.db.refresh(quantity_product)
        return quantity_product

    def quantity_product_delete(self, product_id: int):
        quantity_product = self.get_quantity_product_one(product_id)

        if not quantity_product:
            return None

        self.db.delete(quantity_product)
        self.db.commit()
        return quantity_product
