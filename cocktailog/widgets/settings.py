"""
Author: Gregg Oliva
"""
# 3rd-party imports
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button, Select, Static, Switch, TabbedContent

# project imports
from widgets.base import ButtonIds, TabIds, Title


class SettingLabel(Static):
    pass


class SettingsScreen(Static):
    # CSS classes
    SETTING_ROW_CLASS = "settings_tab_setting_row"
    BUTTON_ROW_CLASS = "settings_tab_button_row"

    # widget IDs
    THEME_SELECT_ID = "settings_tab_theme_select_id"

    def compose(self) -> ComposeResult:
        yield Title("Settings")
        yield Horizontal(
            SettingLabel("Dark Mode:"),
            Switch(value=True, id="dark_mode"),
            classes=self.SETTING_ROW_CLASS,
        )
        yield Horizontal(
            SettingLabel("Theme:"),
            Select(
                (("Default", "default"), ("Theme1", "theme1"), ("Theme2", "theme2")),
                allow_blank=False,
                value="default",
                id=self.THEME_SELECT_ID,
            ),
            classes=self.SETTING_ROW_CLASS,
        )
        yield Horizontal(
            Button(
                ButtonIds.HOME.name,
                id=ButtonIds.HOME.id,
            ),
            classes=self.BUTTON_ROW_CLASS,
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
