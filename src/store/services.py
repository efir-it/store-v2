from sqlalchemy.orm import Session

from . import model, schema


class StoreService:
    def __init__(self, db: Session):
        self.db = db

    def get_store_one(self, store_id: int):
        return self.db.query(model.Store).filter(model.Store.id == store_id).first()

    def get_store_all(self):
        return self.db.query(model.Store).all()

    def get_store_create(self, data: schema.Store):
        store = model.Store(name=data.name, address=data.address, separated=data.separated, rmk_id=data.rmk_id)
        self.db.add(store)
        self.db.commit()
        self.db.refresh(store)
        return store

    def get_store_update(self, product_id: int, data: schema.Store):
        store = self.get_store_one(product_id)
        if not store:
            return None

        for key, value in store.items():
            setattr(store, key, value)

        self.db.commit()
        self.db.refresh(store)
        return store

    def get_store_delete(self, product_id: int):
        store = self.get_store_one(product_id)

        if not store:
            return None

        self.db.delete(store)
        self.db.commit()
        return store
