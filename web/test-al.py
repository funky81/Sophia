from sqlalchemy import *
from sqlalchemy.orm import create_session
from sqlalchemy.ext.declarative import declarative_base
import pdb

#Create and engine and get the metadata
Base = declarative_base()
engine = create_engine('sqlite:///../SophiaDB')
metadata = MetaData(bind=engine)

#Reflect each database table we need to use, using metadata
class Tests(Base):
  __table__ = Table('NodeInfo', metadata, autoload=True)

class Users(Base):
  __table__ = Table('Nodes', metadata, autoload=True)
      
        #Create a session to use the tables
session = create_session(bind=engine)
        #Here I will just query some data using my foreign key relation,  as you would
        #normally do if you had created a declarative data mode.
        #Note that not all test records have an author so I need to accomodate for Null records
testlist = session.query(Users).all()    
        
for test in testlist:
 # testauthor = session.query(Users).filter_by(NodeId=test.NodeId).first()  
 # if not testauthor:
 #   print "Test Name: {}, No author recorded".format(test.Temp)
 # else:
  print "Test Name: {}, Test Author: {}".format(test.NodeId, test.Name)