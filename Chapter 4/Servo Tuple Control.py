from machine import Pin, PWM
import time

servo = PWM(Pin(0))
servo.freq(50)
movement = (2, 5, 8)
while True:
    for i in movement:
        servo.duty_u16(i * 1000[jo1.1][GU1.2])
        time.sleep(2)
