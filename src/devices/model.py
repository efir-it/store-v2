from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from ..drivers.model import drivers_devices
Base = declarative_base()


class Devices(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(200), nullable=False)
    hide = Column(Boolean)

    drivers = relationship('drivers',
                           backref='devices',
                           secondary=drivers_devices,
                           # back_populates="devices"
                           )

    rmk_id = Column(Integer, ForeignKey('rmk.id'))

    type_device_id = Column(Integer, ForeignKey('type_device.id'))
