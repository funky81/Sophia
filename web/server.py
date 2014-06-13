from datetime import datetime
import sqlite3
import re
from flask import g
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('app.cfg')
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
  return 'Hello World'

@app.route('/temp')
def temp_page():
  return render_template('template/temperature.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0')