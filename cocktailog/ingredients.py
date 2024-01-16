"""
Author: Gregg Oliva
"""
# stdlib imports
from enum import Enum
from hashlib import md5

# project imports
from db import tables
from db.api import db

# mypy imports
from typing import Dict, List


class IngredientType(Enum):
    SPIRIT = "spirit"
    LIQUEUR = "liqueur"
    WINE = "wine"
    BEER = "beer"
    BITTERS = "bitters"
    JUICE = "juice"
    SYRUP = "syrup"
    GARNISH = "garnish"
    OTHER = "other"


class Ingredient:
    def __init__(
            self,
            category: IngredientType,
            type: str,
            style: str = None,
            brand: str = None,
            notes: str = None
        ) -> None:
        self.category = category
        self.type = type
        self.style = style
        self.brand = brand
        self.notes = notes
        self.id = str(self.__hash__())

    @property
    def db_kwargs(self) -> None:
        return {
            'id': self.id,
            'category': self.category.value,
            'type': self.type,
            'style': self.style,
            'brand': self.brand,
            'notes': self.notes,
        }

    def write_to_db(self) -> None:
        ingredient_entry = tables.Ingredients(**self.db_kwargs)
        db.insert(ingredient_entry)

    def __hash__(self) -> int:
        str_to_hash = self.category.value + self.type

        if self.style is not None:
            str_to_hash += self.style

        if self.brand is not None:
            str_to_hash += self.brand

        if self.notes is not None:
            str_to_hash += self.notes

        return int(md5(str_to_hash.encode('utf-8'), usedforsecurity=False).hexdigest(), 16)

    def __repr__(self) -> str:
        details = [
            f"{self.category.value.capitalize()}",
            f"\tType: {self.type.capitalize()}",
        ]

        if self.style is not None:
            details.append(
                f"\tStyle: {self.style.capitalize()}",
            )

        if self.brand is not None:
            details.append(
                f"\tBrand: {self.brand.capitalize()}",
            )

        return "\n".join(details)

    def __str__(self) -> str:
        return str(self.__repr__())


class IngredientSearch:
    def __init__(self, ingredient: Ingredient, include_style: bool = False, include_brand: bool = False) -> None:
        self.ingredient: Ingredient = ingredient
        self.include_style: bool = include_style
        self.include_brand: bool = include_brand

    def equals(self, other: Ingredient) -> bool:
        is_identical = self.ingredient.category == other.category and self.ingredient.type == other.type

        if self.include_style:
            is_identical = is_identical and self.ingredient.style == other.style

        if self.include_brand:
            is_identical = is_identical and self.ingredient.brand == other.brand

        return is_identical


class IngredientManager:
    CATEGORY_TO_CLASS = {
        IngredientType.SPIRIT.value: IngredientType.SPIRIT,
        IngredientType.LIQUEUR.value: IngredientType.LIQUEUR,
        IngredientType.WINE.value: IngredientType.WINE,
        IngredientType.BEER.value: IngredientType.BEER,
        IngredientType.BITTERS.value: IngredientType.BITTERS,
        IngredientType.JUICE.value: IngredientType.JUICE,
        IngredientType.SYRUP.value: IngredientType.SYRUP,
        IngredientType.GARNISH.value: IngredientType.GARNISH,
        IngredientType.OTHER.value: IngredientType.OTHER,
    }

    def __init__(self) -> None:
        self.recipe_ingredients = {}
        self.available_ingredients = {}

    def get_by_id(self, id: str) -> Ingredient:
        return self.recipe_ingredients[id]

    def add_ingredient(self, *ingredients: List[Ingredient]) -> None:
        for ingredient in ingredients:
            self.recipe_ingredients[ingredient.id] = ingredient

    def add_available_ingredient(self, *ingredients: List[Ingredient]) -> None:
        for ingredient in ingredients:
            self.available_ingredients[ingredient.id] = ingredient

    def load_all_from_db(self) -> None:
        rows = db.session.query(tables.Ingredients)
        for row in rows:
            ingredient = Ingredient(
                category=self.CATEGORY_TO_CLASS[row.category],
                type=row.type,
                style=row.style,
                brand=row.brand,
                notes=row.notes,
            )
            self.add_ingredient(ingredient)

        rows = db.session.query(tables.AvailableIngredients)
        for row in rows:
            ingredient = self.get_by_id(row.ingredient_id)
            self.add_available_ingredient(ingredient)
