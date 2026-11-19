import tkinter as tk
import serial

#for Windows may need to change to reflect your actual port
#port = "COM3"
#for Mac double check with ls /dev/cu.* in terminal 
#port = "/dev/cu.usbmodem101"

ser = serial.Serial(port, 115200, timeout=1)

root = tk.Tk()
root.geometry("250x150")

label = tk.Label(root, text="0", font=("Arial", 30))
label.pack()

def update():
    if ser.in_waiting:
        text = ser.readline().decode().strip()
        label.config(text=text)
    root.after(50, update)

def start():
    ser.write(b"START\r\n")
    ser.flush()
    update()
    
def stop():
    ser.write(b"STOP\r\n")
    ser.flush()

tk.Button(root,
          text="Start",
          command=start,
          width=20).pack(pady=10)

tk.Button(root,
          text="Stop",
          command=stop,
          width=20).pack(pady=10)

root.mainloop()
ser.close()
