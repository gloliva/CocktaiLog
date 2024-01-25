"""
Author: Gregg Oliva
"""
# 3rd-party imports
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button, Select, Static, Switch, TabbedContent

# project imports
from widgets.base import ButtonIds, TabIds, Title


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
        yield Button(
            ButtonIds.HOME.name,
            id=ButtonIds.HOME.id,
        )

    def on_switch_changed(self, event: Switch.Changed) -> None:
        switch_id = event.switch.id
        switch_value = event.value

        if switch_id == "dark_mode":
            self.app.dark = switch_value

    def on_button_pressed(self, event: Button.Pressed):
        button_id = event.button.id

        if button_id == ButtonIds.HOME.id:
            tabs = self.app.query_one(f"#{TabIds.TAB_MANAGER.id}", TabbedContent)
            tabs.active = TabIds.HOME.id
