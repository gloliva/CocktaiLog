"""
Author: Gregg Oliva
"""
# 3rd-party imports
from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import (
    Button,
    Collapsible,
    Input,
    OptionList,
    SelectionList,
    Static,
    TabbedContent,
    TabPane,
)
from textual.widgets.option_list import Option

# project imports
from widgets.base import ButtonIds, TabIds


class IngredientSearchTabs(Static):
    INGREDIENT_SEARCH_ID = "ingredient_search_list"

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("Tab One"):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(use_selection_format=True),
                    id=self.INGREDIENT_SEARCH_ID,
                )
            with TabPane("Tab Two"):
                yield Static()


class RecipeHomeScreen(Static):
    RECIPE_LIST_ID = "recipe_list"
    RECIPE_SEARCH_ID = "recipe_search_input"
    INGREDIENT_SEARCH_ID = "ingredient_search_list"

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
            Collapsible(
                IngredientSearchTabs(),
                title="Search by Ingredients",
                collapsed=True,
            ),
            Button(
                ButtonIds.HOME.name,
                id=ButtonIds.HOME.id,
            )
        )

    def on_button_pressed(self, event: Button.Pressed):
        button_id = event.button.id

        if button_id == ButtonIds.HOME.id:
            tabs = self.app.query_one(f"#{TabIds.TAB_MANAGER.id}", TabbedContent)
            tabs.active = TabIds.HOME.id

    def on_input_changed(self, event: Input.Changed) -> None:
        input_id = event.input.id
        input_value = event.value

        if input_id == self.RECIPE_SEARCH_ID:
            option_list = self.query_one(f"#{self.RECIPE_LIST_ID}", OptionList)
            options = self.app.rm.get_all_recipe_names(prefix=input_value)

            if not options:
                options = [Option(f"No Recipe(s) Found", disabled=True)]

            option_list.clear_options()
            option_list.add_options(options)
