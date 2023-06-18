from typing import List

from sqlalchemy.orm import Session

from .model import Rmk as RmkModel
from .schema import Rmk as RmkSchema


def get_rmk(rmk_id: int, db) -> RmkModel:
    return db.query(RmkModel).filter(RmkModel.id == rmk_id).first()


def get_rmks(db) -> List[RmkModel]:
    return db.query(RmkModel).all()


def create_rmk(rmk: dict, db):
    db_rmk = RmkModel(name=rmk.name)
    db.add(db_rmk)
    db.commit()
    db.refresh(db_rmk)
    return db_rmk


def update_rmk(rmk: RmkModel, rmk_id: int, db) -> RmkModel:
    db_rmk = get_rmk(rmk_id, db)
    db_rmk.name = rmk.name
    db.commit()
    db.refresh(db_rmk)
    return db_rmk


def delete_rmk(rmk_id: int, db) -> RmkModel:
    db_rmk = get_rmk(rmk_id, db)
    db.delete(db_rmk)
    db.commit()
    return db_rmk
