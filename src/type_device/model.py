from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, clear_mappers, configure_mappers, declarative_base

from core.database import Base


# Base = declarative_base()

class TypeDevice(Base):
    __tablename__ = 'type_device'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(200), nullable=False, unique=True)
    # devices = relationship('Devices', backref='type_device')
    # device = relationship("devices", back_populates="type_device", uselist=False)

    class Config:
        orm_mode = True



