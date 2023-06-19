from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from core.database import Base


class Store(Base):
    __tablename__ = 'store'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    address = Column(String(300), nullable=False)
    separated = Column(Boolean, default=True)

    quantity_products = relationship("QuantityProducts", back_populates="store")

