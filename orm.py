from sqlalchemy.orm import mapper, relationship
from sqlalchemy import MetaData, Table, Column, Integer, String

import model

metadata = MetaData()

order_lines = Table(
    "order-lines", metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('sku', String(255)),
    Column('qty', Integer, nullable=False),
    Column('orderid', String(255))
)

def start_mappers():
    # bind our domain model classes to the tables we defined
    lines_mappers = mapper(model.OrderLine, order_lines)