import tkinter as tk
from tkinter import messagebox
import auth
import serial
from time import sleep

#for Windows may need to change to reflect your actual port
#port = "COM3"
#for Mac double check with ls /dev/cu.* in terminal 
port = "/dev/cu.usbmodem101"
ser = serial.Serial(port , 115200, timeout=1)

def login():
    user = username.get()
    pw = password.get()

    pw = auth.hashPassword(pw)
    access = auth.login(user,pw)
    if access:
        messagebox.showinfo("Message", "Welcome!")
        armBtn.config(state="normal")
    else:
        messagebox.showinfo("Message", "Access denied")
        

def newAccount():
    user = username.get()
    pw = password.get()
    
    pw = auth.hashPassword(pw)
    auth.createAccount(user,pw)

def arm():
    launchBtn.config(state="normal")
    status.config(text="ARMED")
    ser.write(b"ARM\n")

def launch():
    ser.write(b"LAUNCH\n")
    sleep(10)
    reset()
    
def reset():
    armBtn.config(state="disabled")
    launchBtn.config(state="disabled")
    status.config(text = "LOGIN")
    ser.write(b"RESET\n")

root = tk.Tk()
root.title("Rocket Launcher")
root.geometry("450x400")

tk.Label(root, text="Username").pack()
username = tk.Entry(root)
username.pack()

tk.Label(root, text="Password").pack()
password = tk.Entry(root, show="*")
password.pack()

# Frame puts the buttons on the same line
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="LOGIN", command=login).pack(
    side="left", padx=5
)

tk.Button(button_frame, text="CREATE ACCOUNT", command=newAccount).pack(
    side="left", padx=5
)

armBtn = tk.Button(
    root, text="ARM", command=arm, state="disabled"
)
armBtn.pack(pady=10)

launchBtn = tk.Button(
    root, text="LAUNCH", command=launch, state="disabled"
)
launchBtn.pack(pady=10)

cancelBtn = tk.Button(
    root, text="Cancel", command=reset
)
cancelBtn.pack(pady=10)

status = tk.Label(root, text="LOGIN")
status.pack()

root.mainloop()
ser.close()
