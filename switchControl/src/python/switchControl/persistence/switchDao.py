MT_SWITCHDB = "MT_SWITCHDB"


class SwitchDao:
    createTableStatement = '''CREATE TABLE IF NOT EXISTS switches (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                pin INTEGER NOT NULL
                            );'''
    getPinForSwitchStatement = "SELECT (pin) FROM switches where id=?"
    getSwitchForPinStatement = "SELECT (switch) FROM switches where pin=?"
    insertStatement = "INSERT INTO switches VALUES (?)"

    def __init__(self, connection):
        self.conn = connection

        cursor = self.conn.cursor()
        cursor.execute(self.createTableStatement)

    def get_pin_for_switch(self, switch):
        cursor = self.conn.cursor()
        cursor.execute(self.getPinForSwitchStatement, (switch,))
        result = cursor.fetchone()
        if result is None:
            raise ValueError("{} is not a valid switch ID".format(switch))
        return result[0]

    def get_switch_for_pin(self, pin):
        cursor = self.conn.cursor()
        cursor.execute(self.getSwitchForPinStatement, (pin,))
        result = cursor.fetchone()
        if result is None:
            return None
        return result[0]

    def insert_switch(self, pin):
        cursor = self.conn.cursor()
        cursor.execute(self.insertStatement, (pin,))
        result = cursor.lastrowid
        self.conn.commit()
        return result
