# from sqlalchemy import MetaData, Integer, String, Table, Column, Boolean, ForeignKey
#
# from sqlalchemy.orm import relationship
#
# metadata = MetaData()
#
# drivers = Table(
#     "drivers",
#     metadata,
#     Column("id", Integer, primary_key=True, nullable=False),
#     Column("name", String(200), nullable=False),
#     Column("position_save", String(200)),
#     Column("model_device", String(200)),
#     Column('type_device_id', Integer, ForeignKey('type_device.id')),
#
# )
#
# drivers_devices = Table(
#     Column("id", Integer, primary_key=True, nullable=False),
#     Column('device_id', Integer, ForeignKey('devices.id')),
#     Column('drivers_id', Integer, ForeignKey('drivers.id')),
# )
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

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
                           secondary=drivers_devices,
                           back_populates="devices"
                           )


# class DriversDevices(Base):
#     __tablename__ = 'drivers_devices'
#     id = Column(Integer, primary_key=True, nullable=False)
#     device_id = Column(Integer, ForeignKey('devices.id'))
#     driver_id = Column(Integer, ForeignKey('drivers.id'))

#

