MT_SWITCHDB = "MT_SWITCHDB"

ID_COLUMN = "id"
PIN_COLUMN = "pin"

class SwitchDao:
    createTableStatement = """CREATE TABLE IF NOT EXISTS switches (
                                {} INTEGER PRIMARY KEY AUTOINCREMENT,
                                {} INTEGER NOT NULL
                            );""".format(ID_COLUMN, PIN_COLUMN)
    getPinForSwitchStatement = "SELECT ({}) FROM switches where {}=?".format(PIN_COLUMN, ID_COLUMN)
    getSwitchForPinStatement = "SELECT ({}) FROM switches where {}=?".format(ID_COLUMN, PIN_COLUMN)
    getSwitchesStatement = "SELECT ({}) FROM switches".format(ID_COLUMN)
    insertStatement = "INSERT INTO switches ({}) VALUES (?)".format(PIN_COLUMN)

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

    def get_all_switches(self):
        cursor = self.conn.cursor()
        cursor.execute(self.getSwitchesStatement)
        return cursor.fetchall()