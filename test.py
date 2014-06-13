from time import sleep
import serial
ser = serial.Serial()
ser.port = "/dev/ttyACM0" # may be called something different
ser.baudrate = 9600 # may be different
ser.open()
i=0
while True:
    #ser.write("hello")
    response = ser.readline()
    print(response)
    #ser.write("01111")
    if "APP" in response:
       print("TEST")
       i+=1
    if i==2:
       print("masuk sini")
       ser.write("02100\n")
       i=0
