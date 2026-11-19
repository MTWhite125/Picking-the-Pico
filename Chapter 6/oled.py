from machine import Pin, I2C
import ssd1306

i2c = I2C(0, scl=Pin(1), sda=Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.text("Hello World!", 0, 0)
oled.show()


