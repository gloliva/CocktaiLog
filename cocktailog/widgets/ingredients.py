"""
Author: Gregg Oliva
"""
# 3rd-party imports
from textual.containers import Vertical
from textual.widgets import Button, Static


class IngredientsScreen(Static):
    def compose(self) -> None:
        yield Vertical(
            Button("Add Ingredient", classes="ingredients_main_menu"),
            Button("Modify Ingredient", classes="ingredients_main_menu"),
            Button("Remove Ingredient", classes="ingredients_main_menu"),
            id="ingredients_main",
        )

