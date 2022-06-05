import ormlite
import sqlite3

main_db = ormlite.Database("db.db")


test_table = ormlite.Table("test324551", main_db.get_cursor())
print(main_db.tables())
