"""
Author: Gregg Oliva
"""
# 3rd-party imports
from textual.containers import Vertical
from textual.widgets import Button, Static, TabbedContent

# project imports
from widgets.base import ButtonIds, TabIds


class IngredientsScreen(Static):
    def compose(self) -> None:
        yield Vertical(
            Button(
                ButtonIds.INGREDIENTS_SEARCH.name,
                id=ButtonIds.INGREDIENTS_SEARCH.id,
            ),
            Button(
                ButtonIds.INGREDIENTS_MODIFY.name,
                id=ButtonIds.INGREDIENTS_MODIFY.id,
            ),
            Button(
                ButtonIds.HOME.name,
                id=ButtonIds.HOME.id,
            ),
            id="ingredients_main",
        )

    def on_button_pressed(self, event: Button.Pressed):
        button_id = event.button.id

        if button_id == ButtonIds.INGREDIENTS_SEARCH.id:
            pass
        elif button_id == ButtonIds.INGREDIENTS_MODIFY.id:
            pass
        elif button_id == ButtonIds.HOME.id:
            tabs = self.app.query_one(f"#{TabIds.TAB_MANAGER.id}", TabbedContent)
            tabs.active = TabIds.HOME.id
