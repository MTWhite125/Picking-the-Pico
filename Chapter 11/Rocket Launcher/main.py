from machine import Pin
import sys
import uselect
import time

ignitor = Pin(0, Pin.OUT)

# Poll for serial input without blocking
poll = uselect.poll()
poll.register(sys.stdin, uselect.POLLIN)
armed = False

while True:
    if poll.poll(10): 
        command = sys.stdin.readline().strip()

        if command == "ARM":
            armed = True
        
        elif (armed == True and command == "LAUNCH"):
            ignitor.value(1)
            
        elif command == "RESET":
            ignitor.value(0)
            armed = False
        
