from flask import render_template
from app import app, models
from models import Nodes

@app.route('/')
def index():
  return "Hello, World!"

@app.route('/index')
def index_with_template():
  user = {'name' : 'Reski'}
  return render_template("index.html",
    title = 'Home',
    user = user)

@app.route('/node/<id>')
def show_node(id):
  node = Nodes.query.filter_by(NodeId=id).first()
  #node = models.Nodes.query.all()
  if node == None:
    flash('Node with ID '+ id + ' not found')
    return redirect(url_for('index'))
  return render_template('node.html',node=node)