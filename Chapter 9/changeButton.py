import tkinter as tk 
root = tk.Tk() 

root.geometry("300x200") 

option1 = tk.BooleanVar() 
option2 = tk.BooleanVar() 
option3 = tk.BooleanVar() 

tk.Checkbutton(root, text="Option1", variable=option1).pack(anchor="w") 
tk.Checkbutton(root, text="Option2", variable=option2).pack(anchor="w") 
tk.Checkbutton(root, text="Option3", variable=option3).pack(anchor="w") 

root.mainloop() 