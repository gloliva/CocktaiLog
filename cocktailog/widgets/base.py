"""
Author: Gregg Oliva
"""
# stdlib imports
from collections import namedtuple

# 3rd-party imports
from textual.widgets import Static


class Title(Static):
    """Used for Titles"""


class TabIds:
    Tab = namedtuple("Tab", ["name", "id"])

    # Tab Names
    TAB_MANAGER = Tab("Tab Manager", "tab_manager")
    HOME = Tab("Home", "home_tab")
    INGREDIENTS = Tab("Ingredients", "ingredients_tab")
    RECIPES = Tab("Recipes", "recipes_tab")
    SETTINGS = Tab("Settings", "settings_tab")


class ButtonIds:
    # Home page
    HOME = "home"
    HOME_INGREDIENTS = "home_ingredients"
    HOME_RECIPES = "home_recipes"
    HOME_SETTINGS = "home_settings"
