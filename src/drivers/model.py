from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base

from core.database import Base

drivers_devices = Table(
    "drivers_devices",
    Base.metadata,
    Column("device_id", ForeignKey("devices.id")),
    Column("driver_id", ForeignKey("drivers.id")),
)


class Driver(Base):
    __tablename__ = 'drivers'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(200), nullable=False)
    position_save = Column(String(200))
    model_device = Column(String(200))

    type_device_id = Column(Integer, ForeignKey('type_device.id'))

    type_device = relationship('TypeDevice')
    devices = relationship('devices',
                           backref='driver',
                           secondary=drivers_devices
                           )

# class DriversDevices(Base):
#     __tablename__ = 'drivers_devices'
#     id = Column(Integer, primary_key=True, nullable=False)
#     device_id = Column(Integer, ForeignKey('devices.id'))
#     driver_id = Column(Integer, ForeignKey('drivers.id'))

#
