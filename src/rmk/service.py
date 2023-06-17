from typing import List

from sqlalchemy.orm import Session

from .model import Rmk
from .schema import Rmk, RmkCreate, RmkUpdate


class RmkService:
    def __init__(self, db: Session):
        self.db = db

    def get_rmk(self, rmk_id: int) -> Rmk:
        return self.db.query(Rmk).filter(Rmk.id == rmk_id).first()

    def get_rmks(self) -> List[Rmk]:
        return self.db.query(Rmk).all()

    def create_rmk(self, rmk: RmkCreate):
        db_rmk = Rmk(name=rmk.name)
        self.db.add(db_rmk)
        self.db.commit()
        self.db.refresh(db_rmk)
        return db_rmk

    def update_rmk(self, rmk: RmkUpdate, rmk_id: int) -> Rmk:
        db_rmk = self.get_rmk(rmk_id)
        db_rmk.name = rmk.name
        self.db.commit()
        self.db.refresh(db_rmk)
        return db_rmk

    def delete_rmk(self, rmk_id: int) -> Rmk:
        db_rmk = self.get_rmk(rmk_id)
        self.db.delete(db_rmk)
        self.db.commit()
        return db_rmk
