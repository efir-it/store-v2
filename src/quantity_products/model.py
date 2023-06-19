from sqlalchemy import Integer, String, Column, Float, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base


class QuantityProducts(Base):
    __tablename__ = 'quantity_products'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    product = Column(String)
    store_id = Column(Integer, ForeignKey('store.id'))
    count = Column(Float, nullable=False, default=0)

    store = relationship("Store", back_populates="quantity_products")


