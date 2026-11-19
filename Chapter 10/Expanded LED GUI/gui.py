import tkinter as tk
import serial

#for Windows may need to change to reflect your actual port
#port = "COM3"
#for Mac double check with ls /dev/cu.* in terminal 
#port = "/dev/cu.usbmodem101"

ser = serial.Serial(port , 115200, timeout=1)

def led_on():
    ser.write(b"ON\n")

def led_off():
    ser.write(b"OFF\n")
    
def led_blink():
    ser.write(b"BLINK\n")
    
def led_toggle():
    ser.write(b"TOGGLE\n")

root = tk.Tk()
root.title("Pico LED Control")
root.geometry("250x250")

tk.Button(root,
          text="LED ON",
          command=led_on,
          width=20).pack(pady=10)

tk.Button(root,
          text="LED OFF",
          command=led_off,
          width=20).pack(pady=10)

tk.Button(root,
          text="LED BLINK",
          command=led_blink,
          width=20).pack(pady=10)

tk.Button(root,
          text="LED TOGGLE",
          command=led_toggle,
          width=20).pack(pady=10)

root.mainloop()
ser.close()

