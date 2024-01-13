"""
Author: Gregg Oliva
"""
# stdlib imports
from enum import Enum

# project imports
from cocktailog.ingredients import Ingredient

# mypy imports
from typing import List, Optional, Union


class Units(Enum):
    OZ = "oz"
    ML = "ml"
    DROP = "drop"
    DASH = "dash"
    TEASPOON = "tsp"
    TABLESPOON = "tbl"
    BARSPOON = "barspoon"
    OTHER = "other"


class RecipeItem:
    def __init__(self, ingredient: Ingredient, amount: Union[float, int], unit: Units) -> None:
        self.ingredient: Ingredient = ingredient
        self.amount = amount
        self.unit = unit


class Recipe:
    def __init__(self, name: str, version: int = 1, items: Optional[List[RecipeItem]] = None) -> None:
        self.name = name
        self.version = version
        self.items: List[RecipeItem] = [] if items is None else items

    def add_items(self, items: List[RecipeItem]) -> None:
        self.items.extend(items)
