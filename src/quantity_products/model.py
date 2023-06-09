# from sqlalchemy import MetaData, Integer, String, Table, Column, Boolean, Float, ForeignKey
#
# from sqlalchemy.orm import relationship
#
# metadata = MetaData()
#
# quantity_products = Table(
#     "quantity_products",
#     metadata,
#     Column("id", Integer, primary_key=True, nullable=False),
#     Column('product_id', Integer, ForeignKey('product.id')),
#     Column('store_id', Integer, ForeignKey('store.id')),
#     Column("count", Float, nullable=False)
# )
#


from sqlalchemy import Integer, String, Column, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
# from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class QuantityProducts(Base):
    __tablename__ = 'quantity_products'

    id = Column(Integer, primary_key=True, nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'))
    store_id = Column(Integer, ForeignKey('store.id'))
    count = Column(Float, nullable=False)

    product = relationship("Product", back_populates="quantities")
    store = relationship("Store", back_populates="quantities")


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    quantities = relationship("QuantityProducts", back_populates="product")
