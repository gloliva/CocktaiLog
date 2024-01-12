"""
Author: Gregg Oliva
"""

# 3rd-part imports
from sqlalchemy import Column, String, Float, Integer, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base


# Base class for models
Base = declarative_base()


# Ingredients
class AlcoholModel(Base):
    __tablename__ = "alcohols"

    id = Column(Integer, primary_key=True)
    category = Column(String)
    type = Column(String)
    style = Column(String)
    brand = Column(String)
    notes = Column(String)


class IngredientModel(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True)
    category = Column(String)
    type = Column(String)
    notes = Column(String)
