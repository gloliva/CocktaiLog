"""
Author: Gregg Oliva
"""
# 3rd-party imports
from typing import Any
from textual.widgets import Static


class Title(Static):
    """Used for Titles"""


class TabIds:
    TAB_MANAGER = "tab_manager"
    HOME = "home_tab"
    INGREDIENTS = "ingredients_tab"
    RECIPES = "recipes_tab"
    SETTINGS = "settings_tab"


class ButtonIds:
    # Home page
    HOME = "home"
    HOME_INGREDIENTS = "home_ingredients"
    HOME_RECIPES = "home_recipes"
    HOME_SETTINGS = "home_settings"
