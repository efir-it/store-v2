from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from core.database import Base


class TypeDevice(Base):
    __tablename__ = 'type_device'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(200), nullable=False)

    device = relationship("Device", back_populates="type_device", uselist=False)
