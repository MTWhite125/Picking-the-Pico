from machine import Pin, SoftI2C 
from time import sleep

i2c = SoftI2C(sda=Pin(0), scl=Pin(1), freq=9600)

#write to Arduino
def writeToArduino(cmd):
    writeCmd = None

    if cmd == 1:
        writeCmd = b'\x01'
    elif cmd == 2:
        writeCmd = b'\x02'
    elif cmd == 3:
        writeCmd = b'\x03'
    elif cmd == 4:
        writeCmd = b'\x04'
    elif cmd == 5:
        writeCmd = b'\x05'
    elif cmd == 6:
        writeCmd = b'\x06'
    elif cmd == 7:
        writeCmd = b'\x07'
    else:
        print("command not found")
        return

    i2c.writeto(0x08, writeCmd)

# Wait for Uno
print("Waiting for Arduino")
while 0x08 not in i2c.scan():
    sleep(0.5)
    
print ("""
Arduino Found!
1: Turn on red LED
2: Turn on green LED
3: Flash green LED
4: Flash red LED
5: Turn on both LEDs
6: Turn off both LEDs
7: Alt Flash LEDs
""")

while True:
    command = int(input("Please Enter Mode: "))
    writeToArduino(command)
