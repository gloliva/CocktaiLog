"""
Author: Gregg Oliva
"""
# stdlib imports
from collections import namedtuple

# 3rd-party imports
from textual.widgets import Static


class Title(Static):
    """Used for Titles"""


Id = namedtuple("Id", ["name", "id"])


class TabIds:
    # Primary
    TAB_MANAGER = Id("Tab Manager", "primary_tab_manager")
    HOME = Id("Home", "primary_home_tab")
    BUILD = Id("Build", "primary_build_tab")
    SEARCH = Id("Search", "primary_search_tab")
    SETTINGS = Id("Settings", "primary_settings_tab")

    # Recipe Ingredient Search tabs
    RECIPE_TAB_MANAGER = Id("Recipe Tab Manager", "recipe_tab_manager")
    RECIPE_SPIRIT = Id("Spirits", "recipe_spirit_tab")
    RECIPE_LIQUEUR = Id("Liqueurs", "recipe_liqueur_tab")
    RECIPE_WINE = Id("Wine", "recipe_wine_tab")
    RECIPE_BEER = Id("Beer", "recipe_beer_tab")
    RECIPE_BITTERS = Id("Bitters", "recipe_bitters_tab")
    RECIPE_JUICE = Id("Juice", "recipe_juice_tab")
    RECIPE_SYRUP = Id("Syrups", "recipe_syrup_tab")
    RECIPE_WATER = Id("Water", "recipe_water_tab")
    RECIPE_HERB = Id("Herbs", "recipe_herb_tab")
    RECIPE_GARNISH = Id("Garnishes", "recipe_garnish_tab")
    RECIPE_OTHER = Id("Other", "recipe_other_tab")


class ButtonIds:
    # All pages
    HOME = Id("Home", "home_button")
    BACK = Id("Go Back", "back_button")

    # Home page
    HOME_BUILD = Id("Build", "home_tab_build")
    HOME_SEARCH = Id("Search", "home_tab_search")
    HOME_SETTINGS = Id("Settings", "home_settings")

    # Build page
    INGREDIENTS_SEARCH = Id("Search Ingredient(s)", "ingredients_search")
    INGREDIENTS_MODIFY = Id("Add / Update Ingredient(s)", "ingredients_modify")

    # Search page
    RECIPE_SEARCH = Id("Search Recipe(s)", "recipes_search")
    RECIPE_MODIFY = Id("Add / Update Recipe(s)", "recipes_modify")
