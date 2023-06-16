from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

from core.database import Base
# Base = declarative_base()


class Devices(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(200), nullable=False)
    hide = Column(Boolean)

    drivers = relationship('drivers')

    rmk_id = Column(Integer, ForeignKey('rmk.id'))
    type_device_id = Column(Integer, ForeignKey('type_device.id'))

    class Config:
        orm_mode = True
