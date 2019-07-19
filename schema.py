
import sqlite3
import sys
import os
from model.todoitem import TodoItem, CREATE_SQL

TABLENAME = TodoItem.dbtable
DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), "todo.db")


def create_table(dbpath):
    DROP_SQL = "DROP TABLE IF EXISTS {};".format(TABLENAME)

    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        cur.execute(DROP_SQL)
        cur.execute(CREATE_SQL)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        dbname = sys.argv[1]
    else:
        dbname = "todo.db"
    dbpath = os.path.join(os.path.dirname(__file__), dbname)
    create_table(dbpath)
