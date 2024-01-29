"""
Author: Gregg Oliva
"""
# 3rd-party imports
from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import (
    Button,
    Collapsible,
    Input,
    OptionList,
    Select,
    SelectionList,
    Static,
    TabbedContent,
    TabPane,
)
from textual.widgets.option_list import Option

# project imports
from ingredients import IngredientType, IngredientSearch, IngredientSearchMode
from widgets.base import ButtonIds, TabIds


class IngredientSearchTabs(Static):
    NUM_TABS = 11

    # CSS classes
    SEARCH_TAB_CLASS = "search_tab_ingredient_search_tab_panes"
    INGREDIENT_SELECTION_CLASS = "search_tab_ingredient_search_selection_lists"

    # widget IDs
    SELECTION_IDS = [
        f"search_tab_ingredient_search_selection_list_id_{selection_id}"
        for selection_id in range(NUM_TABS)
    ]

    def compose(self) -> ComposeResult:
        with TabbedContent(initial=TabIds.RECIPE_SPIRIT.id, id=TabIds.RECIPE_TAB_MANAGER.id):
            with TabPane(TabIds.RECIPE_SPIRIT.name, id=TabIds.RECIPE_SPIRIT.id, classes=self.SEARCH_TAB_CLASS):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.SPIRIT,
                    ),
                    id=self.SELECTION_IDS[0],
                    classes=self.INGREDIENT_SELECTION_CLASS,
                )
            with TabPane(TabIds.RECIPE_LIQUEUR.name, id=TabIds.RECIPE_LIQUEUR.id, classes=self.SEARCH_TAB_CLASS):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.LIQUEUR,
                    ),
                    id=self.SELECTION_IDS[1],
                    classes=self.INGREDIENT_SELECTION_CLASS,
                )
            with TabPane(TabIds.RECIPE_WINE.name, id=TabIds.RECIPE_WINE.id, classes=self.SEARCH_TAB_CLASS):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.WINE,
                    ),
                    id=self.SELECTION_IDS[2],
                    classes=self.INGREDIENT_SELECTION_CLASS,
                )
            with TabPane(TabIds.RECIPE_JUICE.name, id=TabIds.RECIPE_JUICE.id, classes=self.SEARCH_TAB_CLASS):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.JUICE,
                    ),
                    id=self.SELECTION_IDS[3],
                    classes=self.INGREDIENT_SELECTION_CLASS,
                )
            with TabPane(TabIds.RECIPE_SYRUP.name, id=TabIds.RECIPE_SYRUP.id, classes=self.SEARCH_TAB_CLASS):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.SYRUP,
                    ),
                    id=self.SELECTION_IDS[4],
                    classes=self.INGREDIENT_SELECTION_CLASS,
                )
            with TabPane(TabIds.RECIPE_BITTERS.name, id=TabIds.RECIPE_BITTERS.id, classes=self.SEARCH_TAB_CLASS):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.BITTERS,
                    ),
                    id=self.SELECTION_IDS[5],
                    classes=self.INGREDIENT_SELECTION_CLASS,
                )
            with TabPane(TabIds.RECIPE_BEER.name, id=TabIds.RECIPE_BEER.id, classes=self.SEARCH_TAB_CLASS):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.BEER,
                    ),
                    id=self.SELECTION_IDS[6],
                    classes=self.INGREDIENT_SELECTION_CLASS,
                )
            with TabPane(TabIds.RECIPE_GARNISH.name, id=TabIds.RECIPE_GARNISH.id, classes=self.SEARCH_TAB_CLASS):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.GARNISH,
                    ),
                    id=self.SELECTION_IDS[7],
                    classes=self.INGREDIENT_SELECTION_CLASS,
                )
            with TabPane(TabIds.RECIPE_HERB.name, id=TabIds.RECIPE_HERB.id, classes=self.SEARCH_TAB_CLASS):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.HERB,
                    ),
                    id=self.SELECTION_IDS[8],
                    classes=self.INGREDIENT_SELECTION_CLASS,
                )
            with TabPane(TabIds.RECIPE_WATER.name, id=TabIds.RECIPE_WATER.id, classes=self.SEARCH_TAB_CLASS):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.WATER,
                    ),
                    id=self.SELECTION_IDS[9],
                    classes=self.INGREDIENT_SELECTION_CLASS,
                )
            with TabPane(TabIds.RECIPE_OTHER.name, id=TabIds.RECIPE_OTHER.id, classes=self.SEARCH_TAB_CLASS):
                yield SelectionList(
                    *self.app.im.get_all_ingredient_names(
                        use_selection_format=True,
                        sort_results=True,
                        category_filter=IngredientType.OTHER,
                    ),
                    id=self.SELECTION_IDS[10],
                    classes=self.INGREDIENT_SELECTION_CLASS,
                )


class IngredientSearchScreen(Static):
    # CSS classes
    OPTIONS_ROW = "search_tab_options_row"
    OPTIONS_LABEL = "search_tab_options_label"

    # widget Ids
    INGREDIENT_SEARCH_OPTION_LIST_ID = "search_tab_selected_ingredient_option_list"
    INGREDIENT_SEARCH_INPUT_ID = "search_tab_ingredient_search_input"
    INGREDIENT_SEARCH_SELECT_MODE_ID = "search_tab_selected_ingredients_select_mode"
    INGREDIENT_SEARCH_OPTION_ROW_ID = "search_tab_ingredient_search_options_row"

    def compose(self) -> ComposeResult:
        yield OptionList(
            Option("No Ingredient(s) Selected", disabled=True),
            id=self.INGREDIENT_SEARCH_OPTION_LIST_ID,
        )
        yield Input(
            placeholder="Search Ingredients",
            id=self.INGREDIENT_SEARCH_INPUT_ID,
        )
        yield Horizontal(
            Static("Search Mode:", classes=self.OPTIONS_LABEL),
            Select(
                (
                    ("Ingredient -> Recipe Match", IngredientSearchMode.INGREDIENTS_MATCH),
                    ("Recipe -> Ingredient Match",  IngredientSearchMode.RECIPE_MATCH),
                    ("Exact Match", IngredientSearchMode.EXACT_MATCH),
                ),
                allow_blank=False,
                value=IngredientSearchMode.INGREDIENTS_MATCH,
                id=self.INGREDIENT_SEARCH_SELECT_MODE_ID,
            ),
            Static("Sort By:", classes=self.OPTIONS_LABEL),
            id=self.INGREDIENT_SEARCH_OPTION_ROW_ID,
        )
        yield IngredientSearchTabs()

    def on_selection_list_selected_changed(self, event: SelectionList.SelectedChanged):
        # Update ingredients list
        option_list = self.app.query_one(f"#{self.INGREDIENT_SEARCH_OPTION_LIST_ID}", OptionList)

        self.app.im.update_selected_ingredients(
            event.selection_list.id,
            event.selection_list.selected,
        )

        options = self.app.im.get_selected_ingredients(name_only=True)

        if not options:
            options = [Option(f"No Ingredient(s) Selected", disabled=True)]

        option_list.clear_options()
        option_list.add_options(options)


class SearchScreen(Static):
    # CSS classes
    BUTTON_ROW_CLASS = "search_tab_button_row"

    # widget Ids
    RECIPE_SEARCH_ID = "search_tab_cocktail_search_input"
    RECIPE_LIST_ID = "search_tab_cocktail_option_list"
    INGREDIENTS_SEARCH_COLLAPSIBLE_ID = "search_tab_ingredient_collapsible"
    RECIPE_HOME_BUTTON_ID = "search_tab_home_button"

    # Search Screen Variables
    search_mode = None

    def on_mount(self) -> None:
        select = self.query_one(f"#{IngredientSearchScreen.INGREDIENT_SEARCH_SELECT_MODE_ID}", Select)
        self.search_mode = select.value

    def compose(self) -> ComposeResult:
        yield VerticalScroll(
            Input(
                placeholder="Search by Name",
                id=self.RECIPE_SEARCH_ID,
            ),
            OptionList(
                *self.app.rm.get_all_recipe_names(),
                id=self.RECIPE_LIST_ID,
            ),
            Collapsible(
                IngredientSearchScreen(),
                title="Search by Ingredients",
                collapsed=True,
                id=self.INGREDIENTS_SEARCH_COLLAPSIBLE_ID,
            ),
            Horizontal(
                Button(
                    ButtonIds.HOME.name,
                    id=self.RECIPE_HOME_BUTTON_ID,
                ),
                classes=self.BUTTON_ROW_CLASS,
            ),
        )

    def on_button_pressed(self, event: Button.Pressed):
        button_id = event.button.id

        if button_id == self.RECIPE_HOME_BUTTON_ID:
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

    def on_select_changed(self, event: Select.Changed):
        select_id = event.select.id

        if select_id == IngredientSearchScreen.INGREDIENT_SEARCH_SELECT_MODE_ID:
            self.search_mode = event.select.value

    def on_selection_list_selected_changed(self, _: SelectionList.SelectedChanged):
        # Update ingredients list
        option_list = self.app.query_one(f"#{self.RECIPE_LIST_ID}", OptionList)

        selected_ingredients = self.app.im.get_selected_ingredients()
        ingredients_to_search = [
            IngredientSearch(
                ingredient,
                include_style=True,
                include_brand=True,
            )
            for ingredient in selected_ingredients
        ]

        if not ingredients_to_search:
            option_list.clear_options()
            option_list.add_options(self.app.rm.get_all_recipe_names())
            return

        recipes = self.app.rm.search_by_ingredients(ingredients_to_search, self.search_mode)

        if not recipes:
            options = [Option(f"No Recipe(s) Found", disabled=True)]
        else:
            options = [recipe.name for recipe in recipes]

        option_list.clear_options()
        option_list.add_options(options)
