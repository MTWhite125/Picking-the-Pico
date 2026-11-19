from machine import Pin, I2C
from pico_i2c_lcd import I2cLcd
import time

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=100000)

print(i2c.scan())

lcd = I2cLcd(i2c, 0x27, 2, 16)

lcd.backlight_on()
lcd.clear()
lcd.putstr("Picking the Pico!")
lcd.move_to(0, 1)
lcd.putstr("Packt Ltd")
