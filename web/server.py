import sqlite3
from flask import g
from flask import Flask
app = Flask(__name__)

DATABASE = '../SophiaDB'

def get_db():
  db = getattr(g,'_database',None)
  if db is None :
    db = g._database = sqlite3.connect(DATABASE)
  return db
  
@app.teardown_appcontext
def close_connection(exception):
  db = getattr(g,'_database',None)
  if db is not None:
    db.close()
 
@app.route('/')
def hello_world():
  return 'Hello World'

@app.route('/temp')
def temp_page():
  return render_template('template/temperature.html'

if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0')