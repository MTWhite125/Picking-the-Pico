from machine import Pin 
from random import randint 
from time import sleep 

redLed = Pin(0, Pin.OUT)    #wrong 
greenLed = Pin(1, Pin.OUT)  #You win 
yellowLed = Pin(2, Pin.OUT) #too low 
blueLed = Pin(3, Pin.OUT)   #too high 

num = randint(1,10) 
userGuess = None 

while (userGuess != num): 
    userGuess = int(input("Please enter a number between 1 and 10: ")) 

    redLed.low() 
    greenLed.low() 
    yellowLed.low() 
    blueLed.low() 

    if userGuess > num: 
        blueLed.high() 
        for i in range(10): 
            redLed.high() 
            sleep(.1) 
            redLed.low() 
            sleep(.1) 

    elif userGuess < num: 
        yellowLed.high() 
        for i in range(10): 
            redLed.high() 
            sleep(.1) 
            redLed.low() 
            sleep(.1) 

    elif userGuess == num: 
        for i in range(20): 
            greenLed.high() 
            sleep(.1) 
            greenLed.low() 
            sleep(.1) 