
from .jun_orm import Sqlite3ORM

TABLENAME = 'todoitems'

CREATE_SQL = """
CREATE TABLE {tablename} (
    pk INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(256) NOT NULL,
    description TEXT,
    status);
""".format(tablename=TABLENAME)


class TodoItem(Sqlite3ORM):

    fields = ['title', 'description', 'status']
    dbtable = TABLENAME

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.title = kwargs.get('title')
        self.description = kwargs.get('description')
        self.status = kwargs.get('status')

    def json(self):
        return {
            'pk': self.pk,
            'title': self.title,
            'description': self.description,
            'status': self.status
        }
