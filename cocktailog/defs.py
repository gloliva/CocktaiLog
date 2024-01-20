"""
Author: Gregg Oliva
"""
# stdlib imports
import os

# Filepath
PATH = os.path.dirname(os.path.abspath(__file__))

# Database
DB_NAME = "cocktailog.db"
DB_DIRECTORY = os.path.join(PATH, "..", "etc")
DB_FILEPATH = os.path.join(DB_DIRECTORY, DB_NAME)

SQLITE_ENGINE = f"sqlite:///{DB_FILEPATH}"

# Styles
STYLES_DIRECTORY = os.path.join(PATH, "..", "styles")
STYLES_FILE = "cocktailog.tcss"
STYLES_FILEPATH = os.path.join(STYLES_DIRECTORY, STYLES_FILE)

# Json Export
JSON_EXPORT_FILENAME = 'cocktailog_recipes.json'
