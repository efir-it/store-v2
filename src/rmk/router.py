from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .service import RmkService
from .schema import Rmk, RmkCreate, RmkUpdate
from core.database import get_db_session

router = APIRouter(prefix='/rmk', tags=['RMK'])


@router.get('/', response_model=List[Rmk])
def read_rmks(db: Session = Depends(get_db_session)):
    """
    Возвращает список RMK.
    """
    return RmkService(db).get_rmks()


@router.get('/{rmk_id}', response_model=Rmk)
def read_rmk(rmk_id: int, db: Session = Depends(get_db_session)):
    """
    Возвращает RMK по ID.
    """
    rmk = RmkService(db).get_rmk(rmk_id=rmk_id)
    if rmk is None:
        raise HTTPException(status_code=404, detail='RMK not found')
    return rmk


@router.post('/', response_model=Rmk)
def create_rmk(rmk: RmkCreate, db: Session = Depends(get_db_session)):
    """
    Создает новый RMK.
    """
    db_rmk = RmkService(db).create_rmk(rmk)
    return db_rmk


@router.put('/{rmk_id}', response_model=Rmk)
def update_rmk(rmk_id: int, rmk: RmkUpdate, db: Session = Depends(get_db_session)):
    """
    Обновляет RMK.
    """
    db_rmk = RmkService(db).update_rmk(rmk, rmk_id)
    return db_rmk


@router.delete('/{rmk_id}', response_model=Rmk)
def delete_rmk(rmk_id: int, db: Session = Depends(get_db_session)):
    """
    Удаляет RMK.
    """
    db_rmk = RmkService(db).delete_rmk(rmk_id)
    return db_rmk
