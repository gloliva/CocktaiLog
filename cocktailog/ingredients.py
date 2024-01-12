"""
Author: Gregg Oliva
"""

from enum import Enum


class Ingredients(Enum):
    SPIRIT = "spirit"
    LIQUEUR = "liqueur"
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
        self.type = type
        self.style = style
        self.brand = brand
        super().__init__(notes=notes)


class Spirit(Alcohol):
    def __init__(self, type: str, style: str = None, brand: str = None, notes: str = None) -> None:
        self.category = Ingredients.SPIRIT
        super().__init__(type=type, style=style, brand=brand, notes=notes)


class Liqueur(Alcohol):
    def __init__(self, type: str, style: str = None, brand: str = None, notes: str = None) -> None:
        self.category = Ingredients.LIQUEUR
        super().__init__(type=type, style=style, brand=brand, notes=notes)


class Bitters(Alcohol):
    def __init__(self, type: str, style: str = None, brand: str = None, notes: str = None) -> None:
        self.category = Ingredients.BITTERS
        super().__init__(type=type, style=style, brand=brand, notes=notes)


class Juice(Ingredient):
    def __init__(self, type: str, notes: str = None) -> None:
        self.category = Ingredients.JUICE
        super().__init__(type=type, notes=notes)


class Syrup(Ingredient):
    def __init__(self, type: str, notes: str = None) -> None:
        self.category = Ingredients.SYRUP
        super().__init__(type=type, notes=notes)


class Garnish(Ingredient):
    def __init__(self, type: str, notes: str = None) -> None:
        self.category = Ingredients.GARNISH
        super().__init__(type=type, notes=notes)


class Other(Ingredient):
    def __init__(self, type: str, notes: str = None) -> None:
        self.category = Ingredients.OTHER
        super().__init__(type=type, notes=notes)
