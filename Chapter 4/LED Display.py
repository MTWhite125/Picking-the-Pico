from machine import Pin
import time

a = Pin(0, Pin.OUT)
b = Pin(1, Pin.OUT)
c = Pin(2, Pin.OUT)
d = Pin(3, Pin.OUT)
e = Pin(4, Pin.OUT)
f = Pin(5, Pin.OUT)
g = Pin(6, Pin.OUT)
dot = Pin(7, Pin.OUT)

displayNumbers = {
    0: [a, b, c, d, e, f],
    1: [b, c],
    2: [a, b, g, e, d],
    3: [a, b, c, d, g],
    4: [f, b, g, c],
    5: [a, f, g, c, d],
    6: [a, f, g, c, d, e],
    7: [a, b, c],
    8: [a, b, c, d, e, f, g],
    9: [a, b, c, d, g, f]
}
        
while True:
    #uncomment this line and comment other for command to make count down  
    # for i in range(9, -1, -1):
    for i in range(10):
        #number 8 has all leds minus the dot 
    #so use 8 as a means to clear display
        leds = displayNumbers[8]
        for led in leds:
            led.value(0)
        dot.value(0)
        
        leds = displayNumbers[i]
        for led in leds:
            led.value(1)
            
        time.sleep(1)
        
    dot.value(1)
    time.sleep(3)

