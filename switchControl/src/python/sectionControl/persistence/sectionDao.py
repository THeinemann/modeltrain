
ID_COLUMN = "id"
PIN_COLUMN = "pin"

class SectionDao:
    createTableStatement = """CREATE TABLE IF NOT EXISTS sections (
                                {} INTEGER PRIMARY KEY AUTOINCREMENT,
                                {} INTEGER NOT NULL
                            );""".format(ID_COLUMN, PIN_COLUMN)
    getPinForSectionStatement = "SELECT ({}) FROM sections where {}=?".format(PIN_COLUMN, ID_COLUMN)
    getSectionForPinStatement = "SELECT ({}) FROM sections where {}=?".format(ID_COLUMN, PIN_COLUMN)
    getSectionsStatement = "SELECT ({}) FROM sections".format(ID_COLUMN)
    insertStatement = "INSERT INTO sections ({}) VALUES (?)".format(PIN_COLUMN)

    def __init__(self, connection):
        self.conn = connection

        cursor = self.conn.cursor()
        cursor.execute(self.createTableStatement)

    def get_pin_for_section(self, section):
        cursor = self.conn.cursor()
        cursor.execute(self.getPinForSectionStatement, (section,))
        result = cursor.fetchone()
        if result is None:
            raise ValueError("{} is not a valid section ID".format(section))
        return result[0]

    def get_section_for_pin(self, pin):
        cursor = self.conn.cursor()
        cursor.execute(self.getSectionForPinStatement, (pin,))
        result = cursor.fetchone()
        if result is None:
            return None
        return result[0]

    def insert_section(self, pin):
        cursor = self.conn.cursor()
        cursor.execute(self.insertStatement, (pin,))
        result = cursor.lastrowid
        self.conn.commit()
        return result

    def get_all_sections(self):
        cursor = self.conn.cursor()
        cursor.execute(self.getSectionsStatement)
        return list(map(lambda x: x[0], cursor.fetchall()))