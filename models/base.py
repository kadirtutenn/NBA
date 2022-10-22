import sqlite3

DB = sqlite3.connect("tutorial.db")


def createTables():
    cursor = DB.cursor()
    cursor.execute()
