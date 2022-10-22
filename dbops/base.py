import sqlite3 as dbapi2


class Base:
    def __init__(self, db_name):
        print("you are hereeeee!!!!")
        self.db_name = db_name
        self.conn = dbapi2.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
