#from sqlalchemy import *
#from sqlalchemy.orm import create_session
#from sqlalchemy.ext.declarative import declarative_base
#import pdb
from app import app
from flask.ext.sqlalchemy import SQLAlchemy
 
#SQLALCHEMY_DATABASE_URI= 'sqlite:///../../SophiaDB'
 

#Create and engine and get the metadata
#base = declarative_base()
#engine = create_engine('sqlite:///../../sophia.db')
#metadata = MetaData(bind=engine)
#session = create_session(bind=engine)

db = SQLAlchemy(app)

#Reflect each database table we need to use, using metadata
#class NodeInfo(db.Model): 
#  __table__ = Table('NodeInfo', metadata, autoload=True)
  
class Nodes(db.Model): 
  __tablename__ = "Nodes"
  NodeId = db.Column(db.Integer, primary_key=True)
  Name = db.Column(db.String(30))
  def __init__ (self, NodeId, Name):
    self.NodeId = NodeId
    self.Name = Name
  
#def init_db(app):
#  db.init_app(app)
#  return app
        