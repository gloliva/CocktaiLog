"""
Author: Gregg Oliva
"""
# 3rd-party imports
from textual.containers import Horizontal
from textual.widgets import Button, Static, Rule, TabbedContent

# project imports
from widgets.base import ButtonIds, TabIds, Title


class HomeScreen(Static):

    def compose(self) -> None:
        yield Title("Welcome to Cocktailog!")
        yield Rule()
        yield Horizontal(
            Button(ButtonIds.HOME_INGREDIENTS.name, id=ButtonIds.HOME_INGREDIENTS.id),
            Button(ButtonIds.HOME_RECIPES.name, id=ButtonIds.HOME_RECIPES.id),
            Button(ButtonIds.HOME_SETTINGS.name, id=ButtonIds.HOME_SETTINGS.id),
        )

    def on_button_pressed(self, event: Button.Pressed):
        button_id = event.button.id
        tabs = self.app.query_one(TabbedContent)

        if button_id == ButtonIds.HOME_INGREDIENTS.id:
           tabs.active = TabIds.INGREDIENTS.id
        elif button_id == ButtonIds.HOME_RECIPES.id:
            tabs.active = TabIds.RECIPES.id
        elif button_id == ButtonIds.HOME_SETTINGS.id:
            tabs.active = TabIds.SETTINGS.id
