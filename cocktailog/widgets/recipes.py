"""
Author: Gregg Oliva
"""
# 3rd-party imports
from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Button, Static, TabbedContent

# project imports
from widgets.base import ButtonIds, TabIds


class RecipeMainScreen(Static):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Button(
                ButtonIds.RECIPE_SEARCH.name,
                id=ButtonIds.RECIPE_SEARCH.id,
                classes="recipe_buttons",
            ),
            Button(
                ButtonIds.RECIPE_ADD.name,
                id=ButtonIds.RECIPE_ADD.id,
                classes="recipe_buttons",
            ),
            Button(
                ButtonIds.HOME.name,
                id=ButtonIds.HOME.id,
                classes="recipe_buttons",
            ),
        )

    def on_button_pressed(self, event: Button.Pressed):
        button_id = event.button.id

        if button_id == ButtonIds.RECIPE_SEARCH.id:
            pass
        elif button_id == ButtonIds.RECIPE_ADD.id:
            pass
        elif button_id == ButtonIds.HOME.id:
            tabs = self.app.query_one(TabbedContent)
            tabs.active = TabIds.HOME.id
