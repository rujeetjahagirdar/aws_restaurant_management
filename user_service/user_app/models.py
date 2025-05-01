from sqlalchemy import Column, Integer, String
from .db import db


class User(db.Model):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(100), nullable=False)
    user_contact = Column(String(20), nullable=False)
    user_email = Column(String(100), nullable=False, unique=True)