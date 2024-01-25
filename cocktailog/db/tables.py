"""
Author: Gregg Oliva
"""

# 3rd-part imports
from sqlalchemy import (
    Column,
    ForeignKey,
    Float,
    Integer,
    PrimaryKeyConstraint,
    String,
)
from sqlalchemy.orm import declarative_base


# Base class for models
Base = declarative_base()


# Define tables
class Ingredients(Base):
    __tablename__ = "ingredients"

    id = Column(String, primary_key=True)
    category = Column(String, nullable=False)
    type = Column(String, nullable=False)
    style = Column(String)
    brand = Column(String)
    infusion = Column(String)
    notes = Column(String)


class AvailableIngredients(Base):
    __tablename__ = "available_ingredients"

    ingredient_id = Column(String, ForeignKey("ingredients.id"), primary_key=True)


class Recipes(Base):
    __tablename__ = "recipes"

    name = Column(String, nullable=False)
    version = Column(Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint("name", "version"),
    )


class RecipeItems(Base):
    __tablename__ = "recipe_items"

    recipe_name = Column(String, ForeignKey("recipes.name"), nullable=False)
    recipe_version = Column(Integer,  ForeignKey("recipes.version"), nullable=False)
    ingredient_id = Column(String, ForeignKey("ingredients.id"), nullable=False)
    amount = Column(Float, nullable=False)
    unit = Column(String, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint("recipe_name", "recipe_version", "ingredient_id"),
    )
