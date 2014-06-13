#!/usr/bin/env python
from time import sleep
import sqlite3 as lite
import serial
import datetime
#import pdb

class Node:
    def __init__(self,info):
        self.info=info
        self.id = 0
        self.temp=0
        self.humid=0
        self.batt=0.0
    def getInfo(self):
        self.info = self.info.replace('\n','')
        if self.info.find("APP Received")==-1:
            return None
        #print self.info
        #pdb.set_trace()
        arr=self.info.split(" ",7)
        print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print arr
        arr[7]=arr[7].replace('from ','')
        self.id=int(arr[7])
        self.temp=int(arr[4].replace("/",""))
        x=arr[5].split("/")
        self.humid=x[0]
        self.batt=float(x[1].replace(",","."))            

def writeNodeInfo(node):
    con = lite.connect("SophiaDB")
    with con:
        try:
            cur = con.cursor()
            cur.execute( "insert into NodeInfo (NodeId, Temp, Humidity, BatteryInfo,CreateDate) values (?,?,?,?,datetime('now','localtime'))",
                    (node.id,node.temp,node.humid,node.batt));
            con.commit()
        except lite.Error, e:
            print e.message
            if con:
                con.rollback()
            
ser = serial.Serial()
ser.port = "/dev/ttyACM0" # may be called something different
ser.baudrate = 9600 # may be differe...
ser.open()
i=0
while True:
    #ser.write("hello")
    response = ser.readline()
    print response+'',
    if not response.find("APP Received")==-1:
    #ser.write("01111")
        x = Node(response)
        x.getInfo()
        #print x.id
        writeNodeInfo(x)
    #if "APP" in response:
    #   print("TEST")
    #   i+=1
    #if i==2:
    #   print("masuk sini")
    #   ser.write("02100\n")
    #   i=0
