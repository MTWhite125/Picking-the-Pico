from machine import Pin, time_pulse_us
from time import sleep_us, sleep

trig = Pin(1, Pin.OUT)
echo = Pin(0, Pin.IN)

while True:
    trig.low()
    sleep_us(2)

    trig.high()
    sleep_us(10)
    trig.low()

    t = time_pulse_us(echo, 1)

    distance = t * 0.0343 / 2
    print(distance)

    sleep(0.5)

