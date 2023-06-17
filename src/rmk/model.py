from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

from core.database import Base


class Rmk(Base):
    __tablename__ = 'rmk'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    class Config:
        orm_mode = True
