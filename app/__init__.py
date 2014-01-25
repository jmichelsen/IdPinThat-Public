import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask.ext.cacheify import init_cacheify
from config import basedir

app = Flask(__name__)

def bootstrap_it(app):
	Bootstrap(app)
	return app

app = bootstrap_it(app)

cache = init_cacheify(app)

app.config.from_object('config')

from app import views
