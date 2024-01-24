"""
Author: Gregg Oliva
"""
# 3rd-party imports
from textual.containers import Horizontal
from textual.widgets import Button, Static, Rule, TabbedContent

# project imports
from widgets.base import ButtonIds, Title


class HomeScreen(Static):

    def compose(self) -> None:
        yield Title("Welcome to Cocktailog!")
        yield Rule()
        yield Horizontal(
            Button("Ingredients", id=ButtonIds.HOME_INGREDIENTS),
            Button("Recipes", id=ButtonIds.HOME_RECIPES),
            Button("Settings", id=ButtonIds.HOME_SETTINGS),
        )

    def on_button_pressed(self, event: Button.Pressed):
        button_id = event.button.id
        tabs = self.app.query_one(TabbedContent)

        if button_id == ButtonIds.HOME_INGREDIENTS:
           tabs.active = "ingredients"
        elif button_id == ButtonIds.HOME_RECIPES:
            tabs.active = "recipes"
        elif button_id == ButtonIds.HOME_SETTINGS:
            tabs.active = "settings"
