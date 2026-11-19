from machine import Pin 
import time 

#GPIO Setup 
led = Pin(2, Pin.OUT)   
button = Pin(1, Pin.IN, Pin.PULL_UP) 

while True: 
    led.value(not button.value()) 