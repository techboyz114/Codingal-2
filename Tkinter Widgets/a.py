from tkinter import *
from tkinter import messagebox

T = Tk()
T.geometry("200x200")

def msg():
    messagebox.showwarning("Alert!!", "Virus Threat")
    messagebox.showinfo("Alert!!", "Virus Threat")
    messagebox.showerror("Alert!!", "Virus Threat")
    messagebox.askquestion("Alert!!", "Virus Threat")
    messagebox.askokcancel("Alert!!", "Virus Threat")
    messagebox.askyesno("Alert!!", "Virus Threat")
    messagebox.askretrycancel("Alert!!", "Virus Threat")

def win():
    top = Toplevel()  # create a new window
    top.geometry("200x300")
    L = Label(top, text="Label inside sub window")
    L.pack()
    top.mainloop()

L = Label(T, text="Label in main window")
L.place(x=40, y=40)

B = Button(T, text="Scan for Virus", command=msg)
B.place(x=40, y=80)

B = Button(T, text="Click here to open new window", command=win)
B.place(x=40, y=120)

T.mainloop()
