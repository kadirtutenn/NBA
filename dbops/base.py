import sqlite3 as dbapi2


def create_query(txt, obje):
    for i in obje.__dict__.keys():
        print(i)
        txt = txt + ", ?"
    txt = txt + ")"
    return txt


def create_args(obje):
    args = obje.__dict__
    args.pop("id")
    return tuple(args.values())


class Base:
    def __init__(self, db_name, table_name):
        print("hereee")
        self.table_name = table_name
        self.db_name = db_name
        # self.conn = dbapi2.connect(self.db_name, check_same_thread=False)
        # self.cursor = self.conn.cursor()

    def delete(self, id):
        print(f"DELETE FROM {self.table_name} WHERE id=?")
        # self.cursor.execute(f"DELETE FROM {self.table_name} WHERE id=?", (id,))
        # self.conn.commit()

    def get_by_id(self, id):
        print(f"SELECT * FROM {self.table_name} WHERE id=?")
        # self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE id=?", (id,))
        # return self.cursor.fetchone()

    def create(self, object):
        print(
            create_query(f"INSERT INTO {self.table_name} VALUES(NULL,", object),
            create_args(object),
        )
        # self.cursor.execute(
        #     create_query("INSERT INTO users VALUES(NULL,", object), create_args(object)
        # )
        pass
