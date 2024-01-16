"""
Author: Gregg Oliva
"""
# stdlib imports
import os

# Filepath
PATH = os.path.dirname(os.path.abspath(__file__))

# Database
DB_NAME = "cocktailog.db"
DB_DIRECTORY = os.path.join(PATH, "../..", "etc")
DB_FILEPATH = os.path.join(DB_DIRECTORY, DB_NAME)

SQLITE_ENGINE = f"sqlite:///{DB_FILEPATH}"
