import tkinter as tk 

def change_text(): 

    label.config(text="Goodbye") 

root = tk.Tk() 

label = tk.Label(root, text="Hello") 
label.pack() 

button = tk.Button(root, text="Change", command=change_text) 
button.pack() 

root.mainloop() 