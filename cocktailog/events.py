"""
Author: Gregg Oliva
"""
# 3rd-party imports
from prompt_toolkit.key_binding import KeyBindings


KEY_BINDINGS = KeyBindings()


@KEY_BINDINGS.add('c-q')
def quit_app(event):
    event.app.exit()
