from sqlalchemy import Column, Integer, String
from .db import db

class Order(db.Model):
    __tablename__ = "order"

    order_id = Column(Integer, primary_key=True)
    order_status = Column(String(100), nullable=False)
    order_user_id = Column(String(100), nullable=False)
    order_total_price = Column(String(100), nullable=False)
    order_payment_id = Column(String(100), nullable=True)

class OrderItem(db.Model):
    __tablename__ = 'order_item'

    order_item_id = Column(Integer, primary_key=True)
    order_id = Column(String(100), nullable=False)
    item_id = Column(String(100), nullable=False)
    item_quantity = Column(Integer, nullable=False)
    order_item_notes = Column(String(100), nullable=True)