#with filter values 
import time
import serial     
import datetime     
import RPi.GPIO as GPIO
import string
import re

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)

ser = serial.Serial(
              
	port='/dev/ttyAMA0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0.09
)

                
while 1:
	
	now=datetime.datetime.now()
        y=now.strftime("%S")
	x=ser.readline()
	#print x

	z=re.sub('[^0-9]', '', x)
	print z
	