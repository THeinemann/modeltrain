import sqlite3
import os

MT_SWITCHDB = "MT_SWITCHDB"


def get_sqlite_connection(dbfile = None):
    if dbfile is None:
        dbfile = os.environ[MT_SWITCHDB]
    return sqlite3.connect(dbfile)