import sqlite3
from xdg import BaseDirectory

DEFAULT_DB_FILE = "modeltrains.db"

def get_database_file(configuration):
    if "database" in configuration:
        return configuration["database"]

    return "{}/{}".format(BaseDirectory.xdg_data_home, DEFAULT_DB_FILE)

def get_sqlite_connection(configuration):
    dbfile = get_database_file(configuration)
    return sqlite3.connect(dbfile)