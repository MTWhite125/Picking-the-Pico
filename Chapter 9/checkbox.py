from tkinter import * 

def convert(): 
    if c.get() != "": 
        answer.config(text=str(float(c.get()) * 9/5 + 32) + " F") 
    elif f.get() != "": 
        answer.config(text=str((float(f.get()) - 32) * 5/9) + " C") 

def clear(): 
    c.delete(0, END) 
    f.delete(0, END) 
    answer.config(text="") 

root = Tk() 
Label(root, text="C").grid(row=0, column=0) 
c = Entry(root) 
c.grid(row=0, column=1) 

Label(root, text="F").grid(row=1, column=0) 

f = Entry(root) 
f.grid(row=1, column=1) 

Button(root, text="Enter", command=convert).grid(row=2, column=0) 
Button(root, text="Cancel", command=clear).grid(row=2, column=3) 

# Large output label on the right 
answer = Label(root, text="", font=("Arial", 20)) 
answer.grid(row=0, column=2, rowspan=3, padx=20) 
answer.config(text=str(0)) 

root.mainloop() 