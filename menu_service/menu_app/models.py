from sqlalchemy import Column, Integer, String
from .db import db

class MenuItem(db.Model):
    __tablename__ = "menuitem"

    item_id = Column(Integer, primary_key=True)
    item_name = Column(String(100), nullable=False)
    item_price = Column(String(100), nullable=False)
    item_ingredients = Column(String(100), nullable=True)
    item_calories = Column(String(100), nullable=True)