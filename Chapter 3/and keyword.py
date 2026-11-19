from machine import Pin 
from time import sleep 

redLed = Pin(0, Pin.OUT) 
greenLed = Pin(1, Pin.OUT) 
blueLed = Pin(3, Pin.OUT) 

while True: 

    val1 = int(input("Input value 1: ")) 
    val2 = int(input("Input value 2: ")) 

    if val1 < 5 and val2 < 5: 
        greenLed.high() 
        blueLed.low() 

    elif val1 >= 5 and val2 >= 5: 
        blueLed.high() 
        greenLed.low() 

    else: 
        blueLed.low() 
        redLed.low() 
        for i in range(10): 
            redLed.toggle() 
            sleep(1) 