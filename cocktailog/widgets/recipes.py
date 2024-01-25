"""
Author: Gregg Oliva
"""
# 3rd-party imports
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import (
    Button,
    ContentSwitcher,
    Input,
    OptionList,
    Static,
    TabbedContent,
)
from textual.widgets.option_list import Option

# project imports
from widgets.base import ButtonIds, TabIds


class SearchMenu(Static):
    RECIPE_LIST_ID = "recipe_list"
    RECIPE_SEARCH_ID = "recipe_search_input"

    def compose(self) -> ComposeResult:
        yield Input(
            placeholder="Search by Name...",
            id=self.RECIPE_SEARCH_ID,
        )
        yield OptionList(
            *self.app.rm.get_all_recipe_names(),
            id=self.RECIPE_LIST_ID,
        )
        yield Vertical(
            Button(
                "TEST",
                id=ButtonIds.RECIPE_SEARCH.id,
            ),
            Button(
                "TEST TWO",
                id=ButtonIds.RECIPE_MODIFY.id,
            )
        )
        yield Horizontal(
            Button(
                ButtonIds.BACK.name,
                id=ButtonIds.BACK.id,
            ),
            Button(
                ButtonIds.HOME.name,
                id=ButtonIds.HOME.id,
            ),
        )

    def on_button_pressed(self, event: Button.Pressed):
        button_id = event.button.id
        main_menu = self.app.query_one(RecipeMainScreen)

        if button_id == ButtonIds.BACK.id:
            self.parent.current = main_menu.MAIN_ID
        elif button_id == ButtonIds.HOME.id:
            self.parent.current = main_menu.MAIN_ID
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


class MainMenu(Static):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Button(
                ButtonIds.RECIPE_SEARCH.name,
                id=ButtonIds.RECIPE_SEARCH.id,
                classes="recipe_buttons",
            ),
            Button(
                ButtonIds.RECIPE_MODIFY.name,
                id=ButtonIds.RECIPE_MODIFY.id,
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
            self.parent.current = "recipes_search_menu"
        elif button_id == ButtonIds.RECIPE_MODIFY.id:
            pass
        elif button_id == ButtonIds.HOME.id:
            tabs = self.app.query_one(TabbedContent)
            tabs.active = TabIds.HOME.id


class RecipeMainScreen(Static):
    MAIN_ID = "recipes_main_menu"
    SEARCH_ID = "recipes_search_menu"

    def compose(self) -> ComposeResult:
        yield ContentSwitcher (
            MainMenu(
                id=self.MAIN_ID,
            ),
            SearchMenu(
                id=self.SEARCH_ID,
            ),
            initial=self.MAIN_ID,
        )
