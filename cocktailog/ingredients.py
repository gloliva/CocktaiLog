"""
Author: Gregg Oliva
"""
# stdlib imports
from enum import Enum
from hashlib import md5

# 3rd-party imports
from sortedcontainers import SortedDict

# project imports
from db import tables
from db.api import Database
from helpers import capitalize_all

# mypy imports
from typing import Dict, List, Union


class IngredientType(Enum):
    SPIRIT = "spirit"
    LIQUEUR = "liqueur"
    WINE = "wine"
    BEER = "beer"
    BITTERS = "bitters"
    JUICE = "juice"
    SYRUP = "syrup"
    WATER = "water"
    HERB = "herb"
    GARNISH = "garnish"
    OTHER = "other"


class Ingredient:
    CATEGORY_TO_CLASS = {
        IngredientType.SPIRIT.value: IngredientType.SPIRIT,
        IngredientType.LIQUEUR.value: IngredientType.LIQUEUR,
        IngredientType.WINE.value: IngredientType.WINE,
        IngredientType.BEER.value: IngredientType.BEER,
        IngredientType.BITTERS.value: IngredientType.BITTERS,
        IngredientType.JUICE.value: IngredientType.JUICE,
        IngredientType.SYRUP.value: IngredientType.SYRUP,
        IngredientType.WATER.value: IngredientType.WATER,
        IngredientType.HERB.value: IngredientType.HERB,
        IngredientType.GARNISH.value: IngredientType.GARNISH,
        IngredientType.OTHER.value: IngredientType.OTHER,
    }

    def __init__(
            self,
            category: Union[IngredientType, str],
            type: str,
            style: str = None,
            brand: str = None,
            infusion: str = None,
            notes: str = None,
        ) -> None:
        self.category = category if isinstance(category, IngredientType) else self.CATEGORY_TO_CLASS[category]
        self.type = type
        self.style = style
        self.brand = brand
        self.infusion = infusion
        self.notes = notes
        self.id = str(self.__hash__())

    @property
    def db_kwargs(self) -> Dict[str, str]:
        return {
            "id": self.id,
            "category": self.category.value,
            "type": self.type,
            "style": self.style,
            "brand": self.brand,
            "infusion": self.infusion,
            "notes": self.notes,
        }

    @property
    def json_kwargs(self) -> Dict[str, str]:
        return {
            "category": self.category.value,
            "type": self.type,
            "style": self.style,
            "brand": self.brand,
            "infusion": self.infusion,
            "notes": self.notes,
        }

    @property
    def full_name(self) -> str:
        name_parts = []

        if self.infusion is not None:
            name_parts.append(f"{self.infusion}-infused")

        if self.brand is not None:
            name_parts.append(self.brand)

        if self.style is not None:
            name_parts.append(self.style)

        name_parts.append(self.type)
        name = capitalize_all(" ".join(name_parts))

        return name

    def write_to_db(self, db: Database) -> None:
        ingredient_entry = tables.Ingredients(**self.db_kwargs)
        db.insert(ingredient_entry)


    def __hash__(self) -> int:
        str_to_hash = self.category.value + self.type

        if self.style is not None:
            str_to_hash += self.style

        if self.brand is not None:
            str_to_hash += self.brand

        if self.infusion is not None:
            str_to_hash += self.infusion

        return int(md5(str_to_hash.encode("utf-8"), usedforsecurity=False).hexdigest(), 16)

    def __repr__(self) -> str:
        details = []

        if self.infusion is not None:
            details.append(
                f"{capitalize_all(self.infusion)}-infused"
            )

        if self.brand is not None:
            details.append(
                f"{capitalize_all(self.brand)}",
            )

        if self.style is not None:
            details.append(
                f"{capitalize_all(self.style)}",
            )

        details.extend([
            f"{capitalize_all(self.type)}",
            f"{self.category.value.capitalize()}",
        ])

        return " ".join(details)

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

    def __repr__(self) -> str:
        style = "x" if self.include_style else " "
        brand = "x" if self.include_brand else " "
        return f"({self.ingredient} | Search by Style[{style}] Brand[{brand}]"

    def __str__(self) -> str:
        return str(self.__repr__())


class IngredientManager:
    def __init__(self, db: Database) -> None:
        self.db = db
        self.recipe_ingredients: Dict[str, Ingredient] = {}
        self.available_ingredients: Dict[str, Ingredient] = {}
        self.selected_ingredients = SortedDict()

    def get_by_id(self, id: str) -> Ingredient:
        return self.recipe_ingredients[id]

    def add_recipe_ingredient(self, *ingredients: List[Ingredient]) -> None:
        for ingredient in ingredients:
            self.recipe_ingredients[ingredient.id] = ingredient

    def add_available_ingredient(self, *ingredients: List[Ingredient]) -> None:
        for ingredient in ingredients:
            self.available_ingredients[ingredient.id] = ingredient

    def get_all_ingredient_names(
            self,
            include_style: bool = True,
            include_brand: bool = True,
            use_only_available: bool = False,
            category_filter: IngredientType | None = None,
            sort_results: bool = False,
            use_selection_format: bool = False,
        ) -> List[str]:
        ingredients = []
        ingredients_to_search = list(self.available_ingredients.values())

        if not use_only_available:
            ingredients_to_search.extend(
                list(self.recipe_ingredients.values())
            )

        for ingredient in ingredients_to_search:
            if category_filter is not None and ingredient.category != category_filter:
                continue

            name_parts = []

            if include_brand and ingredient.brand is not None:
                name_parts.append(ingredient.brand)

            if include_style and ingredient.style is not None:
                name_parts.append(ingredient.style)

            name_parts.append(ingredient.type)
            full_name = capitalize_all(" ".join(name_parts))
            ingredient_name = (full_name, ingredient.id, False) if use_selection_format else full_name

            ingredients.append(ingredient_name)

        if sort_results:
            if use_selection_format:
                ingredients.sort(key=lambda x: x[0])
            else:
                ingredients.sort()

        return ingredients

    def update_selected_ingredients(self, selection_id: str, selected: List[str]):
        selected_ingredients = [
            self.get_by_id(ingredient_id).full_name
            for ingredient_id in selected
        ]
        selected_ingredients.sort()
        self.selected_ingredients[selection_id] = selected_ingredients

    def get_selected_ingredient_names(self):
        ingredient_names = []
        for ingredient_category in self.selected_ingredients.values():
            ingredient_names.extend(ingredient_category)

        return ingredient_names

    def convert_to_json(self) -> Dict[str, List[Dict[str, str]]]:
        outdict = {
            "recipe_ingredients": [],
            "available_ingredients": [],
        }

        for ingredient in self.recipe_ingredients.values():
            outdict["recipe_ingredients"].append(ingredient.json_kwargs)

        for ingredient in self.available_ingredients:
            outdict["available_ingredients"].append(ingredient.json_kwargs)

        return outdict

    def load_all_from_db(self) -> None:
        rows = self.db.session.query(tables.Ingredients)
        for row in rows:
            ingredient = Ingredient(
                category=row.category,
                type=row.type,
                style=row.style,
                brand=row.brand,
                notes=row.notes,
            )
            self.add_recipe_ingredient(ingredient)

        rows = self.db.session.query(tables.AvailableIngredients)
        for row in rows:
            ingredient = self.get_by_id(row.ingredient_id)
            self.add_available_ingredient(ingredient)
