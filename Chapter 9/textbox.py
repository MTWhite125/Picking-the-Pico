import tkinter as tk 

root = tk.Tk() 
root.geometry("300x200") 

selected = tk.StringVar(value="Option1") 

tk.Radiobutton(root, text="Option1", variable=selected, value="Option1").pack(anchor="w") 
tk.Radiobutton(root, text="Option2", variable=selected, value="Option2").pack(anchor="w") 
tk.Radiobutton(root, text="Option3", variable=selected, value="Option3").pack(anchor="w") 

root.mainloop() 