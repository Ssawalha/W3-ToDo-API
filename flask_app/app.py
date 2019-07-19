#!/usr/bin/env python3

from flask import Flask 
from model.jun_orm import Sqlite3ORM

Sqlite3ORM.dbpath = "todo.db"

app = Flask(__name__) #YOU ALWAYS DO THIS | STANDARD FLASK APPS ARE INITIALIZED THIS WAY

#circular imports --> we are importing routes below, in routes we are importing app
from . import routes #NOTE THAT THIS IS HERE (BELOW app = Flask(__name__)) ON PURPOSE because of circular imports

''' good flask book from look at his longer tutorial | migel grinberg ''' # note to self
