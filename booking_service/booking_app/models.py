from sqlalchemy import Column, Integer, String
from .db import db


class Table(db.Model):
    __tablename__ = "table"

    table_id = Column(Integer, primary_key=True)
    table_capacity = Column(Integer, nullable=False)
    table_status = Column(String, nullable=False)

class Booking(db.Model):
    __tablename__ = "booking"

    booking_id = Column(Integer, primary_key=True)
    booking_time = Column(String, nullable=False)
    booking_status = Column(String, nullable=False)
    booking_user_id = Column(String, nullable=False)
    booking_table_id = Column(String(100), nullable=False)
    booking_payment_status = Column(String(100), nullable=True)
    booking_payment_id = Column(String(100), nullable=True)