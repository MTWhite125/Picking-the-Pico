import tkinter as tk 

 
root = tk.Tk() 
root.geometry("300x200") 


button = tk.Button(root, text="Button", width=15, height=2) 
button.pack(pady=20) 

root.mainloop() 