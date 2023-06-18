from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import service
from .schema import Rmk
from core.database import get_db_session

router = APIRouter()


@router.get('/', response_model=List[Rmk])
def read_rmks(db: Session = Depends(get_db_session)):
    """
    Возвращает список RMK.
    """
    return service.get_rmks(db)


@router.get('/{rmk_id}', response_model=Rmk)
def read_rmk(rmk_id: int, db: Session = Depends(get_db_session)):
    """
    Возвращает RMK по ID.
    """
    rmk = service.get_rmk(rmk_id=rmk_id, db=db)
    if rmk is None:
        raise HTTPException(status_code=404, detail='RMK not found')
    return rmk


@router.post('/', response_model=Rmk)
def create_rmk(rmk: Rmk, db: Session = Depends(get_db_session)):
    """
    Создает новый RMK.
    """
    db_rmk = service.create_rmk(rmk, db)
    return db_rmk


@router.put('/{rmk_id}', response_model=Rmk)
def update_rmk(rmk_id: int, rmk: Rmk, db: Session = Depends(get_db_session)):
    """
    Обновляет RMK.
    """
    db_rmk = service.update_rmk(rmk, rmk_id, db)
    return db_rmk


@router.delete('/{rmk_id}', response_model=Rmk)
def delete_rmk(rmk_id: int, db: Session = Depends(get_db_session)):
    """
    Удаляет RMK.
    """
    db_rmk = service.delete_rmk(rmk_id, db)
    return db_rmk
