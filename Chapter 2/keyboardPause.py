from machine import Pin 
import time 

led = Pin(25, Pin.OUT) 
slp = int(input("Please enter blink rate in seconds: ")) 

while True: 
    led.high() 
    time.sleep(slp)  
    led.low()  
    time.sleep(slp) 