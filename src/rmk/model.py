from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

from core.database import Base


class Rmk(Base):
    __tablename__ = 'rmk'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    store_id = Column(Integer, ForeignKey('store.id'), nullable=False)
    store = relationship('Store', back_populates='rmk')
    devices = relationship('Devices')
