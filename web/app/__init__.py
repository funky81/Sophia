from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
#from app import views,models

app = Flask(__name__)
#app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../sophia.db'
#db = SQLAlchemy(app)
#app.config.from_object('app.model')
#app = init_db(app)

from app import views