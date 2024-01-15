"""
Author: Gregg Oliva
"""
# stdlib imports
from enum import Enum
from hashlib import md5

# project imports
from cocktailog.db import tables
from cocktailog.db.api import db
from cocktailog.ingredients import Ingredient, IngredientManager

# mypy imports
from typing import Dict, List, Union


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
    def __init__(self, name: str, version: int = 1) -> None:
        self.name: str = name
        self.version: int = version
        self.items: List[RecipeItem] = []
        self.id = str(self.__hash__())

    @staticmethod
    def hash(name: str, version: int) -> None:
        str_to_hash = name + str(version)
        return int(md5(str_to_hash.encode('utf-8'), usedforsecurity=False).hexdigest(), 16)

    def add_items(self, *items: List[RecipeItem]) -> None:
        self.items.extend(list(items))

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

    def __hash__(self) -> int:
        str_to_hash = self.name + str(self.version)
        return int(md5(str_to_hash.encode('utf-8'), usedforsecurity=False).hexdigest(), 16)


class RecipeManager:
    def __init__(self, ingredient_manager: IngredientManager) -> None:
        self.recipes: Dict[str, Recipe] = {}
        self.ingredient_manager = ingredient_manager

    def get_by_name(self, name: str, version: int = 1) -> Recipe:
        return self.recipes[str(Recipe.hash(name, version))]

    def load_all_from_db(self) -> None:
        recipe_rows = db.session.query(tables.Recipes)
        for recipe_row in recipe_rows:
            recipe = Recipe(
                recipe_row.name,
                recipe_row.version,
            )

            item_rows = (
                db.session.query(tables.RecipeItems)
                .filter(
                    tables.RecipeItems.recipe_name == recipe.name,
                    tables.RecipeItems.recipe_version == recipe.version,
                )
            )

            for item_row in item_rows:
                recipe_item = RecipeItem(
                    ingredient=self.ingredient_manager.get_by_id(item_row.ingredient_id),
                    amount=item_row.amount,
                    unit=item_row.unit,
                )
                recipe.add_items(recipe_item)

            self.recipes[recipe.id] = recipe
