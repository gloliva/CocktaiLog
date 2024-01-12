"""
Author: Gregg Oliva
"""

from enum import Enum


class Ingredients(Enum):
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
        self.category = Ingredients.SPIRIT


class Liqueur(Alcohol):
    def __init__(self, type: str, style: str = None, brand: str = None, notes: str = None) -> None:
        super().__init__(type=type, style=style, brand=brand, notes=notes)
        self.category = Ingredients.LIQUEUR


class Wine(Alcohol):
    def __init__(self, type: str, style: str = None, brand: str = None, notes: str = None) -> None:
        super().__init__(type=type, style=style, brand=brand, notes=notes)
        self.category = Ingredients.WINE


class Beer(Alcohol):
    def __init__(self, type: str, style: str = None, brand: str = None, notes: str = None) -> None:
        super().__init__(type=type, style=style, brand=brand, notes=notes)
        self.category = Ingredients.BEER


class Bitters(Alcohol):
    def __init__(self, type: str, style: str = None, brand: str = None, notes: str = None) -> None:
        super().__init__(type=type, style=style, brand=brand, notes=notes)
        self.category = Ingredients.BITTERS


class Juice(Ingredient):
    def __init__(self, type: str, notes: str = None) -> None:
        super().__init__(type=type, notes=notes)
        self.category = Ingredients.JUICE


class Syrup(Ingredient):
    def __init__(self, type: str, notes: str = None) -> None:
        super().__init__(type=type, notes=notes)
        self.category = Ingredients.SYRUP


class Garnish(Ingredient):
    def __init__(self, type: str, notes: str = None) -> None:
        super().__init__(type=type, notes=notes)
        self.category = Ingredients.GARNISH


class Other(Ingredient):
    def __init__(self, type: str, notes: str = None) -> None:
        super().__init__(type=type, notes=notes)
        self.category = Ingredients.OTHER
