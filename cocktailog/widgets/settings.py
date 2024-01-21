"""
Author: Gregg Oliva
"""
# 3rd-party imports
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static, Switch


class SettingsScreen(Static):
    def compose(self) -> ComposeResult:
        yield Static("[b]Settings\n", classes="settings_label")
        yield Horizontal(
            Static("Dark Mode:", classes="label"),
            Switch(value=True, id="dark_mode"),
            classes="container",
        )
