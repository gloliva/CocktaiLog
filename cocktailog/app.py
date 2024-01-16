"""
Author: Gregg Oliva
"""
# 3rd-party imports
from prompt_toolkit import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import VSplit, Window
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout

# project imports
from events import KEY_BINDINGS


buffer1 = Buffer()  # Editable buffer.

root_container = VSplit([
    # One window that holds the BufferControl with the default buffer on
    # the left.
    Window(content=BufferControl(buffer=buffer1)),

    # A vertical line in the middle. We explicitly specify the width, to
    # make sure that the layout engine will not try to divide the whole
    # width by three for all these windows. The window will simply fill its
    # content by repeating this character.
    Window(width=1, char='|'),

    # Display the text 'Hello world' on the right.
    Window(content=FormattedTextControl(text='Hello world')),
])

layout = Layout(root_container)


class ApplicationManager:
    def __init__(self, key_bindings: KeyBindings) -> None:
        self.key_bindings = key_bindings
        self.app = None

    def init_app(self) -> None:
        self.app = Application(key_bindings=self.key_bindings, layout=layout, full_screen=True)

    def run_app(self) -> None:
        self.app.run()



app_manager = ApplicationManager(KEY_BINDINGS)
