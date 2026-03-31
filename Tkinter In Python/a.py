from tkinter import *
T=Tk()#main window created
T.title("Demo")
T.geometry('400x400')
T.configure(bg='light pink')
L1=Label(text="Enter your name : ",fg='yellow',bg='blue')
E1=Entry(fg='white',bg='black',width=50)
L2=Label(text="Enter your age : ",fg='yellow',bg='blue')
E2=Entry(fg='white',bg='black',width=50)#single line
B1=Button(text="Submit",bg='red',fg='purple')
L3=Label(text="Enter your address : ",fg='yellow',bg='blue')
'''
L1.pack()
E1.pack()
L2.pack()
E2.pack()
L3.pack()
B1.pack()
'''
L1.grid(row=0,column=0)
E1.grid(row=0,column=1,sticky='w')
L2.grid(row=1,column=0)
E2.grid(row=1,column=1,sticky='w')
L3.grid(row=2,column=0)

F=Frame(master=T,relief=GROOVE,borderwidth=15)#FLAT , SUNKEN, GROOVE , RIDGE , RAISED
F.grid(row=2,column=1)
T1=Text(master=F,fg='yellow',bg='green',width=50,height=10)#multi line
T1.pack()

B1.grid(row=3,column=0)
T.mainloop()