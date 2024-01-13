"""
Author: Gregg Oliva
"""
# stdlib imports
import os

# 3rd-part imports
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm.decl_api import DeclarativeBase

# project imports
from cocktailog.db.defs import DB_DIRECTORY, SQLITE_ENGINE
from cocktailog.db.tables import Base


class Database:
    def __init__(self) -> None:
        self.engine = None
        self.meta = Base.metadata
        self.base = Base

    def init_db(self) -> None:
        if not os.path.isdir(DB_DIRECTORY):
            os.makedirs(DB_DIRECTORY)

    def connect(self) -> None:
        self.engine = create_engine(SQLITE_ENGINE)
        self.meta.reflect(bind=self.engine)
        self.session = Session(bind=self.engine)

    def create_tables(self) -> None:
        self.meta.create_all(self.engine)

    def insert(self, entry: DeclarativeBase) -> None:
        self.session.add(entry)
        self.session.commit()


# Database instance
db = Database()
