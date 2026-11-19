from machine import Pin
from time import sleep

redLed = Pin(0, Pin.OUT)
greenLed = Pin(1, Pin.OUT)
yellowLed = Pin(2, Pin.OUT)
blueLed = Pin(3, Pin.OUT)

ledPattern = [] #empty list
keyInput = None

blinkRate = float(input("please enter you blink rate in seconds: "))

while(keyInput != "q"):
    keyInput = input("1=red, 2=green, 3=yellow, 4=blue, q=quit: ")
    
    #check to ensure the input is an LED number
    if (keyInput == "1" or keyInput == "2" or keyInput == "3" or keyInput == "4"):
        ledPattern.append(int(keyInput))

while True:
    redLed.low()
    greenLed.low()
    yellowLed.low()
    blueLed.low()
    
    for i in ledPattern:
                
        #turn on LED from list
        if i == 1:
            redLed.high()
            sleep(blinkRate)
            redLed.low()
        elif i == 2:
            greenLed.high()
            sleep(blinkRate)
            greenLed.low()
        elif i == 3:
            yellowLed.high()
            sleep(blinkRate)
            yellowLed.low()
        elif i == 4:
            blueLed.high()
            sleep(blinkRate)
            blueLed.low()
        sleep(blinkRate)

    #blink leds to denote end of sequence         
    for i in range(2):
        redLed.low()
        greenLed.low()
        yellowLed.low()
        blueLed.low()
        sleep(1)
     
        redLed.high()
        greenLed.high()
        yellowLed.high()
        blueLed.high()
        sleep(1)
