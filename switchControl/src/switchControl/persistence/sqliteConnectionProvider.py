import sqlite3
import logging

LOGGER = logging.getLogger("sqliteConnectionProvider")

def get_sqlite_connection(configuration):
    dbfile = configuration['database']
    LOGGER.info("Using database file %s", dbfile)
    return sqlite3.connect(dbfile, check_same_thread=False)
