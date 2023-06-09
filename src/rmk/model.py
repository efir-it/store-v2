# from sqlalchemy import Table, Column, Integer, String, ForeignKey, Boolean, MetaData
#
# metadata = MetaData()
#
# rmk = Table(
#     "rmk",
#     metadata,
#     Column("id", Integer, primary_key=True, nullable=False),
#     Column("name", String(100), nullable=False),
#     Column('store_id', Integer, ForeignKey('store.id')),
# )

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Rmk(Base):
    __tablename__ = 'rmk'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    store_id = Column(Integer, ForeignKey('store.id'), nullable=False)
    store = relationship('Store', back_populates='rmk')
    devices = relationship('Devices')
