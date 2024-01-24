"""
Author: Gregg Oliva
"""
# 3rd-party imports
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Select, Static, Switch

# project imports
from widgets.base import Title


class SettingsScreen(Static):
    def compose(self) -> ComposeResult:
        yield Title("Settings")
        yield Horizontal(
            Static("Dark Mode:", classes="label"),
            Switch(value=True, id="dark_mode"),
            classes="container",
        )
        yield Horizontal(
            Static("Theme:", classes="label"),
            Select(
                (("Default", "default"), ("Theme1", "theme1"), ("Theme2", "theme2")),
                allow_blank=False,
                value="default",
                id="themes",
            ),
            classes="container",
        )

    def on_switch_changed(self, event: Switch.Changed) -> None:
        switch_id = event.switch.id
        switch_value = event.value

        if switch_id == "dark_mode":
            self.app.dark = switch_value
