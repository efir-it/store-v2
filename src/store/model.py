from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base

from core.database import Base


class Store(Base):
    __tablename__ = 'store'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    rmk = relationship('Rmk', back_populates='store')
