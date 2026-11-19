import tkinter as tk
import serial

#for Windows may need to change to reflect your actual port
#port = "COM3"
#for Mac double check with ls /dev/cu.* in terminal 
#port = "/dev/cu.usbmodem101"

ser = serial.Serial(port , 115200, timeout=1)

root = tk.Tk()
root.geometry("150x150")

label = tk.Label(root, text="0", font=("Arial", 30))
label.pack()

def update():
    if ser.in_waiting:
        label.config(text=ser.readline().decode().strip())
    root.after(50, update)

update()
root.mainloop()
ser.close()
