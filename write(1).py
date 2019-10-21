
import time
import serial
import datetime
          
ser = serial.Serial(
              
    port='/dev/ttyAMA0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
counter=0
          
while 1:
	now=datetime.datetime.now()
        a=now.strftime("%S")
	b=now.strftime("%M")
	c=now.strftime("%H")
	print a
	ser.write(a)        
        #print("sent on",now.strftime("%H:%M:%S:%f"))
	time.sleep(1)
        