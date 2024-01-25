"""
Author: Gregg Oliva
"""
# 3rd-party imports
from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import (
    Button,
    Input,
    OptionList,
    Static,
    TabbedContent,
)
from textual.widgets.option_list import Option

# project imports
from widgets.base import ButtonIds, TabIds


class RecipeHomeScreen(Static):
    RECIPE_LIST_ID = "recipe_list"
    RECIPE_SEARCH_ID = "recipe_search_input"

    def compose(self) -> ComposeResult:
        yield VerticalScroll(
            Input(
                placeholder="Search by Name...",
                id=self.RECIPE_SEARCH_ID,
            ),
            OptionList(
                *self.app.rm.get_all_recipe_names(),
                id=self.RECIPE_LIST_ID,
            ),
            Button(
                ButtonIds.HOME.name,
                id=ButtonIds.HOME.id,
            )
        )

    def on_button_pressed(self, event: Button.Pressed):
        button_id = event.button.id

        if button_id == ButtonIds.HOME.id:
            tabs = self.app.query_one(TabbedContent)
            tabs.active = TabIds.HOME.id

    def on_input_changed(self, event: Input.Changed) -> None:
        input_id = event.input.id
        input_value = event.value

        if input_id == self.RECIPE_SEARCH_ID:
            option_list = self.query_one(OptionList)
            options = self.app.rm.get_all_recipe_names(prefix=input_value)

            if not options:
                options = [Option(f"No Recipe(s) Found", disabled=True)]

            option_list.clear_options()
            option_list.add_options(options)
