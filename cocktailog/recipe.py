"""
Author: Gregg Oliva
"""
# stdlib imports
from enum import Enum

# project imports
from cocktailog.db import tables
from cocktailog.db.api import db
from cocktailog.ingredients import Ingredient

# mypy imports
from typing import Dict, List, Optional, Union


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
        self.name: str = name
        self.version: int = version
        self.items: List[RecipeItem] = [] if items is None else items

    def add_items(self, items: List[RecipeItem]) -> None:
        self.items.extend(items)

    def write_to_db(self) -> None:
        # Add recipe to the database
        recipe_entry = tables.Recipes(
            name=self.name,
            version=self.version,
        )
        db.insert(recipe_entry)

        # Add recipe items to the database
        for item in self.items:
            recipe_item_entry = tables.RecipeItems(
                recipe_name=self.name,
                recipe_version=self.version,
                ingredient_id=item.ingredient.id,
                amount=item.amount,
                unit=item.unit.value,
            )
            db.insert(recipe_item_entry)


class RecipeList:
    def __init__(self) -> None:
        self.recipes: Dict[str, Dict[int, Recipe]] = {}

    def _get_from_db(self, name: str, version: int = 1) -> None:
        res = (
            db.session.query(tables.Recipes, tables.RecipeItems)
            .filter(
                tables.Recipes.name == name,
                tables.Recipes.version == version,
                tables.Recipes.name == tables.RecipeItems.recipe_name,
                tables.Recipes.version == tables.RecipeItems.recipe_version
            )
            .all()
        )

        for item in res:
            print(item)

    def get(self, name: str, version: int = 1):
        recipe = self.recipes.get(name, {})

        if not recipe:
            self._get_from_db(name, version)
