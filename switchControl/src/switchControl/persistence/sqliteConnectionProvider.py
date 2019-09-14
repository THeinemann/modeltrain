import sqlite3
import logging
from xdg import BaseDirectory

DEFAULT_DB_FILE = "modeltrains.db"
LOGGER = logging.getLogger("sqliteConnectionProvider")

def get_database_file(configuration):
    if "database" in configuration:
        return configuration["database"]

    return "{}/{}".format(BaseDirectory.xdg_data_home, DEFAULT_DB_FILE)

def get_sqlite_connection(configuration):
    dbfile = get_database_file(configuration)
    LOGGER.info("Using database file %s", dbfile)
    return sqlite3.connect(dbfile, check_same_thread=False)
