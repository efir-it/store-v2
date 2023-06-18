from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base

from core.database import Base

# Base = declarative_base()
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
    devices = relationship('Devices', backref='driver')

    class Config:
        orm_mode = True

