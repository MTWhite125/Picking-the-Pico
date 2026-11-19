from machine import Pin
import sys
import uselect
import time

led = Pin("LED", Pin.OUT)

# Poll for serial input without blocking
poll = uselect.poll()
poll.register(sys.stdin, uselect.POLLIN)

while True:
    if poll.poll(10): 
        command = sys.stdin.readline().strip()

        if command == "ON":
            led.value(1)

        elif command == "OFF":
            led.value(0)

    time.sleep_ms(10)
