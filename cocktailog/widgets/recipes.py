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
from ingredients import IngredientType
from widgets.base import ButtonIds, TabIds


class IngredientSearchTabs(Static):
    INGREDIENT_SEARCH_ID = "ingredient_search_list"

    def compose(self) -> ComposeResult:
        with TabbedContent(initial=TabIds.RECIPE_SPIRIT.id, id=TabIds.RECIPE_TAB_MANAGER.id):
            with TabPane(TabIds.RECIPE_SPIRIT.name, id=TabIds.RECIPE_SPIRIT.id):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.SPIRIT,
                    ),
                )
            with TabPane(TabIds.RECIPE_LIQUEUR.name, id=TabIds.RECIPE_LIQUEUR.id):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.LIQUEUR,
                    ),
                )
            with TabPane(TabIds.RECIPE_WINE.name, id=TabIds.RECIPE_WINE.id):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.WINE,
                    ),
                )
            with TabPane(TabIds.RECIPE_JUICE.name, id=TabIds.RECIPE_JUICE.id):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.JUICE,
                    ),
                )
            with TabPane(TabIds.RECIPE_SYRUP.name, id=TabIds.RECIPE_SYRUP.id):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.SYRUP,
                    ),
                )
            with TabPane(TabIds.RECIPE_BITTERS.name, id=TabIds.RECIPE_BITTERS.id):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.BITTERS,
                    ),
                )
            with TabPane(TabIds.RECIPE_BEER.name, id=TabIds.RECIPE_BEER.id):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.BEER,
                    ),
                )
            with TabPane(TabIds.RECIPE_GARNISH.name, id=TabIds.RECIPE_GARNISH.id):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.GARNISH,
                    ),
                )
            with TabPane(TabIds.RECIPE_HERB.name, id=TabIds.RECIPE_HERB.id):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.HERB,
                    ),
                )
            with TabPane(TabIds.RECIPE_WATER.name, id=TabIds.RECIPE_WATER.id):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.WATER,
                    ),
                )
            with TabPane(TabIds.RECIPE_OTHER.name, id=TabIds.RECIPE_OTHER.id):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.OTHER,
                    ),
                )


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
