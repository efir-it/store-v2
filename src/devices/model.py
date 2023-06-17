from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from src.type_device.model import TypeDevice
from core.database import Base


# Base = declarative_base()


class Devices(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(200), nullable=False)
    hide = Column(Boolean)

    rmk_id = Column(Integer, ForeignKey('rmk.id'))
    type_device_id = Column(Integer, ForeignKey('type_device.id'))
    # devices = relationship('Devices', backref='type_device')
    # drivers = relationship('Driver', backref='type_device')

    class Config:
        orm_mode = True
