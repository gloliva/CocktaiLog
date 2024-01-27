"""
Author: Gregg Oliva
"""
# stdlib imports
from enum import Enum
from hashlib import md5
from random import choice

# 3rd-party imports
from pygtrie import CharTrie

# project imports
from db import tables
from db.api import Database
from helpers import capitalize_all
from ingredients import Ingredient, IngredientSearch, IngredientManager

# mypy imports
from typing import Any, Dict, List, Union


class Units(Enum):
    OZ = "oz"
    ML = "ml"
    DROP = "drop"
    DASH = "dash"
    TEASPOON = "tsp"
    TABLESPOON = "tbl"
    BARSPOON = "barspoon"
    LEAVES = "leaves"
    OTHER = "other"


class Preparation(Enum):
    SHAKEN = "shaken"
    STIRRED = "stirred"


class RecipeItem:
    UNITS_TO_CLASS = {
        Units.OZ.value: Units.OZ,
        Units.ML.value: Units.ML,
        Units.DROP.value: Units.DROP,
        Units.DASH.value: Units.DASH,
        Units.TEASPOON.value: Units.TEASPOON,
        Units.TABLESPOON.value: Units.TABLESPOON,
        Units.BARSPOON.value: Units.BARSPOON,
        Units.LEAVES.value: Units.LEAVES,
        Units.OTHER.value: Units.OTHER,
    }

    def __init__(self, ingredient: Ingredient, amount: Union[float, int], unit: Union[Units, str]) -> None:
        self.ingredient: Ingredient = ingredient
        self.amount = amount
        self.unit = unit if isinstance(unit, Units) else self.UNITS_TO_CLASS[unit]

    @property
    def json_kwargs(self) -> Dict[str, Any]:
        return {
            "ingredient": self.ingredient.json_kwargs,
            "amount": self.amount,
            "unit": self.unit.value,
        }

    def __repr__(self) -> str:
        return f"({self.amount} {self.unit}) {self.ingredient}"

    def __str__(self) -> str:
        return str(self.__repr__())


class Recipe:
    def __init__(self, name: str, version: int = 1) -> None:
        self.name: str = name
        self.version: int = version
        self.items: List[RecipeItem] = []
        self.id = str(self.__hash__())

    @staticmethod
    def hash(name: str, version: int) -> None:
        str_to_hash = name + str(version)
        return int(md5(str_to_hash.encode("utf-8"), usedforsecurity=False).hexdigest(), 16)

    @property
    def json_kwargs(self) -> Dict[str, Any]:
        items = [
            item.json_kwargs for item in self.items
        ]

        return {
            'name': self.name,
            'version': self.version,
            'items': items,
        }

    def add_items(self, *items: List[RecipeItem]) -> None:
        self.items.extend(list(items))

    def contains_ingredients(self, ingredients_to_search: List[IngredientSearch], strict=False) -> bool:
        for item in self.items:
            equals = False
            for ingredient in ingredients_to_search:
                equals = equals or ingredient.equals(item.ingredient)

            if not equals:
                return False

        return True

    def write_to_db(self, db: Database) -> None:
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
        return int(md5(str_to_hash.encode("utf-8"), usedforsecurity=False).hexdigest(), 16)

    def __repr__(self) -> str:
        version = f" (v{self.version})" if self.version > 1 else ""
        return f"{self.name}{version}"

    def __str__(self) -> str:
        return str(self.__repr__())


class RecipeManager:
    def __init__(self, db: Database, ingredient_manager: IngredientManager) -> None:
        self.db = db
        self.ingredient_manager = ingredient_manager
        self.recipe_names = CharTrie()
        self.recipe_names.enable_sorting()
        self.recipes: Dict[str, Recipe] = {}

    def get_by_name(self, name: str, version: int = 1) -> Recipe:
        return self.recipes[str(Recipe.hash(name, version))]

    def get_all_recipe_names(self, prefix: str = "") -> List[str]:
        try:
            recipe_names = [
                capitalize_all(recipe[0])
                for recipe in self.recipe_names.items(prefix=prefix.lower())
            ]
        except KeyError:
            recipe_names = []

        return recipe_names

    def search_by_ingredients(
            self,
            ingredients_to_search: List[IngredientSearch],
            strict=False,
        ) -> List[Recipe]:
        makeable_recipes = []
        for recipe in self.recipes.values():
            if recipe.contains_ingredients(ingredients_to_search, strict):
                makeable_recipes.append(recipe)

        makeable_recipes.sort(key=lambda x: x.name)
        return makeable_recipes

    def get_random(self) -> Recipe:
        return choice(self.recipes)

    def load_all_from_db(self) -> None:
        recipe_rows = self.db.session.query(tables.Recipes)
        for recipe_row in recipe_rows:
            recipe = Recipe(
                recipe_row.name,
                recipe_row.version,
            )

            item_rows = (
                self.db.session.query(tables.RecipeItems)
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

            self.recipe_names[recipe.name.lower()] = True
            self.recipes[recipe.id] = recipe

    def convert_to_json(self) -> None:
        return [
            recipe.json_kwargs for recipe in self.recipes.values()
        ]
