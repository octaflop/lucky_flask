# -*- coding: utf-8 -*-

from frysauce import app
from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///frysauce.db'
db = SQLAlchemy(app)
