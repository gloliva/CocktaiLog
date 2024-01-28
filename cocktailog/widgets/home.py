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
            Button(ButtonIds.HOME_BUILD.name, id=ButtonIds.HOME_BUILD.id),
            Button(ButtonIds.HOME_SEARCH.name, id=ButtonIds.HOME_SEARCH.id),
            Button(ButtonIds.HOME_SETTINGS.name, id=ButtonIds.HOME_SETTINGS.id),
        )

    def on_button_pressed(self, event: Button.Pressed):
        button_id = event.button.id
        tabs = self.app.query_one(f"#{TabIds.TAB_MANAGER.id}", TabbedContent)

        if button_id == ButtonIds.HOME_BUILD.id:
           tabs.active = TabIds.BUILD.id
        elif button_id == ButtonIds.HOME_SEARCH.id:
            tabs.active = TabIds.SEARCH.id
        elif button_id == ButtonIds.HOME_SETTINGS.id:
            tabs.active = TabIds.SETTINGS.id
