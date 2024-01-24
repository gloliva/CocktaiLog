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
    TAB_MANAGER = Id("Tab Manager", "tab_manager")
    HOME = Id("Home", "home_tab")
    INGREDIENTS = Id("Ingredients", "ingredients_tab")
    RECIPES = Id("Recipes", "recipes_tab")
    SETTINGS = Id("Settings", "settings_tab")


class ButtonIds:
    # All pages
    HOME = Id("Home", "home_button")

    # Home page
    HOME_INGREDIENTS = "home_ingredients"
    HOME_RECIPES = "home_recipes"
    HOME_SETTINGS = "home_settings"

    # Recipes page
    RECIPE_SEARCH = Id("Search Recipe(s)", "search_recipes")
    RECIPE_ADD = Id("Add Recipe(s)", "add_recipes")
