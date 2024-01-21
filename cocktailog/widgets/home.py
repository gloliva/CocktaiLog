"""
Author: Gregg Oliva
"""
# 3rd-party imports
from textual.widgets import Button, LoadingIndicator, Static, Rule


class Title(Static):
    pass


class HomeScreen(Static):
    def compose(self) -> None:
        yield Title("Welcome to Cocktailog!")
        yield Rule()
