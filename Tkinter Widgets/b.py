from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image Window")
root.geometry("400x400")

img = ImageTk.PhotoImage(Image.open("Image1.png"))  # Image1.png

label = Label(root, image=img)
label.pack(pady=20)

entry = Entry(root, width=25)
entry.pack()

root.mainloop()
