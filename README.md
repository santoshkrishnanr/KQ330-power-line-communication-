# KQ330-power-line-communication-
Python program on raspberry pi to communicate on power, using KQ330 PLC (Power Line Communication)

# Basic of KQ330
The PLC can transmit the data via power line, which are suitable for either residential (at-home) or commercial (offices, apartments, hotels, warehouses) network applications, which utilize power lines. No need to install new wires 
this module works  is a single-row 9-pin small-sized high-performance carrier data transceiver module. Specifically designed for reliable transmission of high-speed data in 0V-220V AC/DC and non-powered environments (such as pipelines and earth, a signal line and earth, two signal lines, 12V AC/DC power lines, etc.) And developed cost-effective carrier modules. Suitable for industrial control, railways, community intelligence, smart home, building control, and other applications that require carrier transmission of data. Transmission distance up to 2.5Km (power line). The actual highest carrier rate is 2400 BPS. 
other  features are :
* Supports Both RS232 and TTL Interface.
* Universal supply works over a power line voltage range of 85 to 265 
* VAC, 50~60Hz
* Support QAM 256/64/16, DQPSK,DBPSK and ROBO modulation schemes
* Up to 85 Mbps data rate on the power line    
* 56-bit DES Link Encryption with key management for security.
* Low power consumption
* Operating frequency 120 ~ 135KHZ, interface baud rate 9600bps. The actual baud rate 100bps.
* Receiving sensitivity ≤1mV
* The band rejection ≥ 60 dB  
* Bandwidth ≤10 KHZ    
* Insulation resistance:  500V  ≥ 500M [Omega]
* Power supply: DC + 5V when the receiver: ≤11mA sent ≤230mA
* Power frequency with stand voltage: AC test between GND 3000V 1min no breakdown, no leakage current.
  *-source internet.



## Getting Started

These instructions will give an idea about the pin connection of KQ330 and a basic program to communicate with PLC.

### Prerequisites
* handlinig 230v AC powe wire
* serial communication
* RaspberryPi
* To run Python program :wink:

for the basic of serial communication with only TX-RX between raspberry pi refer * [serial communication](https://github.com/santoshkrishnanr/serial-communication-in-python) 

### wire connection 

A step by step process for running (since i didnt find the data sheet of KQ330 this was made by observing other projects and video)

pin connection   
* there are totally 9 pins as shown 
![](https://github.com/santoshkrishnanr/KQ330-power-line-communication-/blob/master/Kq330.jpg)

   * lets consider 

```
* pin 1 for 230V AC power
* pin 2 for 230V AC power
* pin 3 5V DC supply if its used as transmitter 
* pin 4 GND supply
* pin 5 5V/3.5V DC supply if its used as receiver 
* pin 6 RX pin should be connected to TX of the controller 
* pin 7 TX pin should be connected to RX of the controller 
* pin 8 & 9 i didnt had to use 
```
## Transmitter

Consider running this [write(1).py](https://github.com/santoshkrishnanr/KQ330-power-line-communication-/blob/master/write(1).py) basic program of sending seconds every second using import time  
on one of the Raspberry Pi with transmission connection with KQ330 i.e
```
* pin 1 for 230V AC power
* pin 2 for 230V AC power
* pin 3 5V DC supply if its used as transmitter 
* pin 4 GND supply
* pin 6 RX pin should be connected to TX of the controller 
```


  ### Points to be considered 

* since serial communication is working from tx port and not from USB 
```
port='/dev/ttyAMA0',
```

* baudrate of KQ330 is 9600 as per the specification, but do try with 100  (it works only for 1 second with 5V power )
```
baudrate = 9600,
```

* keep transmitter KQ330 as far as possible while coding if its connected to AC Power line   

:bomb:


## Receiver

Consider running this [read_v1.py](https://github.com/santoshkrishnanr/KQ330-power-line-communication-/blob/master/read_v1.py) basic program for receiving data 
on one of the Raspberry Pi with receiver connection with KQ330 i.e
```
* pin 1 for 230V AC power
* pin 2 for 230V AC power
* pin 5 5V/3.3V DC supply used as Receiver
* pin 4 GND supply
* pin 7 TX pin should be connected to RX of the controller 
```


  ### Points to be considered 

* since serial communication is working from rx port and not from USB 
```
port='/dev/ttyAMA0',
```

* baudrate of KQ330 is 9600 as per the specification, and should be same as tranmitter side.
```
baudrate = 9600,
```
* this re.sub is used to filter the other character and symbols which gets read by disturbance
* to check the [real](https://github.com/santoshkrishnanr/KQ330-power-line-communication-/blob/master/result%20(1).jpeg) value which is received use 
```
print x
```
or to filter other characters from the string use 
```
z=re.sub('[^0-9]', '', x)
```
for other filter options [refer](https://docs.python.org/3/library/re.html)


what i asume  is 
* KQ330 module does not consume 230V power, it adds frequency
* It was able to read after passing 2 pole MCB and a Smart meter.

![](https://github.com/santoshkrishnanr/KQ330-power-line-communication-/blob/master/pi%20with%20KQ330.jpeg)

    * Happy coding !!!


