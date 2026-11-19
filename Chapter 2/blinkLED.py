from machine import Pin 
import time 

led = Pin(25, Pin.OUT)#configure GPIO 25 to be an OUTPUT 

while True: 
    led.toggle()#Blink LED 
    time.sleep(0.5)#Pause for 1/2 seconds 