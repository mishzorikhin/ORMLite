#
# Mish.zor 2022
#

import sqlite3


class Database:

    def __init__(self, database):
        self.database = database
        self.con = sqlite3.connect(self.database)
        self.cursor = self.con.cursor()

    def close(self):
        self.con.close()

    def tables(self):
        self.con = sqlite3.connect(self.database)
        self.cursor = self.con.cursor()
        self.cursor.execute("SELECT name FROM sqlite_master;")
        answer = self.cursor.fetchall()
        reply = []
        for i in answer:
            reply.append(i[0])
        return reply

    def sql(self, request):
        self.cursor.execute(request)

    def get_cursor(self):
        return self.con


class Table:

    def __init__(self, table_name, con):
        self.con = con
        self.cursor = self.con.cursor()
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id)")
        self.con.commit()
