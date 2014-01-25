#!pme/bin/python
from app import app

app.config.from_pyfile('debug.py')
