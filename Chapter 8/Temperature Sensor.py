from machine import SoftI2C, Pin
import time

i2c = SoftI2C(
    sda=Pin(0),
    scl=Pin(1),
    freq=100000
)

while True:
    i2c.writeto(0x70, b'\x78\x66') #Read temperature first
    #i2c.writeto(0x70, b'\x58\xE0') #Read RH first
    
    time.sleep_ms(15)

    data = i2c.readfrom(0x70, 6)

    raw_temp = data[0] * 256 + data[1]
    raw_hum  = data[3] * 256 + data[4]

    temp_c = -45 + 175 * raw_temp / 65536
    temp_f = temp_c * (9/5) + 32
    
    humidity = 100 * raw_hum / 65536

    print(temp_f, "F")
    print(humidity, "%")

    time.sleep(1)
