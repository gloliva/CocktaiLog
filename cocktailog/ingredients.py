"""
Author: Gregg Oliva
"""
# stdlib imports
from enum import Enum
from uuid import uuid4


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
    def __init__(self, type: str, notes: str = None) -> None:
        self.category = None
        self.id = str(uuid4())
        self.type = type
        self.notes = notes


class Alcohol(Ingredient):
    def __init__(self, type: str, style: str = None, brand: str = None, notes: str = None) -> None:
        super().__init__(type=type, notes=notes)
        self.style = style
        self.brand = brand


class Spirit(Alcohol):
    def __init__(self, type: str, style: str = None, brand: str = None, notes: str = None) -> None:
        super().__init__(type=type, style=style, brand=brand, notes=notes)
        self.category = IngredientType.SPIRIT


class Liqueur(Alcohol):
    def __init__(self, type: str, style: str = None, brand: str = None, notes: str = None) -> None:
        super().__init__(type=type, style=style, brand=brand, notes=notes)
        self.category = IngredientType.LIQUEUR


class Wine(Alcohol):
    def __init__(self, type: str, style: str = None, brand: str = None, notes: str = None) -> None:
        super().__init__(type=type, style=style, brand=brand, notes=notes)
        self.category = IngredientType.WINE


class Beer(Alcohol):
    def __init__(self, type: str, style: str = None, brand: str = None, notes: str = None) -> None:
        super().__init__(type=type, style=style, brand=brand, notes=notes)
        self.category = IngredientType.BEER


class Bitters(Alcohol):
    def __init__(self, type: str, style: str = None, brand: str = None, notes: str = None) -> None:
        super().__init__(type=type, style=style, brand=brand, notes=notes)
        self.category = IngredientType.BITTERS


class Juice(Ingredient):
    def __init__(self, type: str, notes: str = None) -> None:
        super().__init__(type=type, notes=notes)
        self.category = IngredientType.JUICE


class Syrup(Ingredient):
    def __init__(self, type: str, notes: str = None) -> None:
        super().__init__(type=type, notes=notes)
        self.category = IngredientType.SYRUP


class Garnish(Ingredient):
    def __init__(self, type: str, notes: str = None) -> None:
        super().__init__(type=type, notes=notes)
        self.category = IngredientType.GARNISH


class Other(Ingredient):
    def __init__(self, type: str, notes: str = None) -> None:
        super().__init__(type=type, notes=notes)
        self.category = IngredientType.OTHER
