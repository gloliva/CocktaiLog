"""
Author: Gregg Oliva
"""
# stdlib imports
import os

# project imports
from defs import STYLES_DIRECTORY

# mypy imports
from typing import List


def capitalize_all(s: str) -> str:
    return " ".join(
        [
            word.capitalize()
            for word in s.split(" ")
        ]
    )


def get_css_files() -> List[str]:
    filenames = os.listdir(STYLES_DIRECTORY)
    style_files = [
        os.path.join(STYLES_DIRECTORY, filename)
        for filename in filenames
        if filename.endswith(".tcss")
    ]

    return style_files
