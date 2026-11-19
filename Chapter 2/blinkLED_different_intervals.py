from machine import Pin 

import time 

led = Pin(25, Pin.OUT)#configure GPIO 25 to be an OUTPUT 

while True: 
    led.high() #Turn LED on  
    time.sleep(1) #Wait with LED on for 1 second 
    led.low() #Turn LED off 
    time.sleep(2) #Wait with LED off for 2 seconds 