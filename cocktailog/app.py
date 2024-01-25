"""
Author: Gregg Oliva
"""
# stdlib imports
import json
import os
import tkinter as tk
from tkinter import filedialog

# 3rd-party imports
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import (
    Footer,
    Header,
    TabbedContent,
    TabPane,
)

# project imports
from db.api import Database
from defs import JSON_EXPORT_FILENAME
from helpers import get_css_files
from ingredients import IngredientManager
from widgets.base import TabIds
from widgets.home import HomeScreen
from widgets.ingredients import IngredientsScreen
from widgets.recipes import RecipeHomeScreen
from widgets.settings import SettingsScreen
from recipe import RecipeManager


class Cocktailog(App[int]):
    CSS_PATH = get_css_files()
    BINDINGS = [
        Binding("q", "quit_app", "Quit App"),
        Binding("ctrl+i", "import_data", "Import data from JSON file"),
        Binding("ctrl+e", "export_data", "Export data from JSON file"),
    ]

    def setup(self) -> None:
        # set up tkinter
        self.tk_root = tk.Tk()
        self.tk_root.withdraw()

        # set up db
        self.db = Database()
        self.db.init_db()
        self.db.connect()
        self.db.create_tables()

        # set up ingredients and recipes
        self.im = IngredientManager(self.db)
        self.rm = RecipeManager(self.db, self.im)

        # load all from db
        self.im.load_all_from_db()
        self.rm.load_all_from_db()

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        with TabbedContent(initial=TabIds.HOME.id, id=TabIds.TAB_MANAGER.id):
            with TabPane(TabIds.HOME.name, id=TabIds.HOME.id):
                yield HomeScreen()
            with TabPane(TabIds.INGREDIENTS.name, id=TabIds.INGREDIENTS.id):
                yield IngredientsScreen()
            with TabPane(TabIds.RECIPES.name, id=TabIds.RECIPES.id):
                yield RecipeHomeScreen()
            with TabPane(TabIds.SETTINGS.name, id=TabIds.SETTINGS.id):
                yield SettingsScreen()

    def action_quit_app(self) -> None:
        self.exit(0, return_code=0)

    def action_import_data(self) -> None:
        pass

    def action_export_data(self) -> None:
        directory = filedialog.askdirectory(title="Select Directory to Write Recipe JSON")
        outfile = os.path.join(directory, JSON_EXPORT_FILENAME)

        outjson = {
            "ingredients": self.im.convert_to_json(),
            "recipes": self.rm.convert_to_json(),
        }

        json.dump(outjson, fp=open(outfile, "w"), sort_keys=True, indent=4)
