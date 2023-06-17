from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

from core.database import Base


class Store(Base):
    __tablename__ = 'store'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(300), nullable=False)
    separated = Column(Boolean)

    rmk_id = Column(Integer, ForeignKey('rmk.id'))
    rmk = relationship('Rmk', back_populates='store')

    class Config:
        orm_mode = True
