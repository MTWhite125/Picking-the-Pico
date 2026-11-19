from machine import Pin 
import time 

#set GPIO pins as outputs for LEDs 
redLed = Pin(0, Pin.OUT) 
greenLed = Pin(1, Pin.OUT) 

while True: 
    greenLed.high() #turn green LED on 
    redLed.low()    #turn red LED off 

    time.sleep(1)   #wait 1 second 

    greenLed.low()  #turn green LED off 
    redLed.high()   #turn red LED on 

    time.sleep(1)   #wait 1 second 