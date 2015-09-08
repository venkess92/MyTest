import sys
from Tkinter import *
from tkFileDialog import *
import tkMessageBox 
mygui = Tk()
ven = Tk()
def new():
	b = a.get()
	myLabel5 = Label(ven,text='Name Entered as '+ b,fg = 'blue').place(x = 10,y = 20)

def mopen():
	fileName = askopenfilename(parent=mygui)

def mnew():
	myLabel6 = Label(text='you pressed View Contacts',fg = 'blue').place(x = 150,y = 50)

def mbox():
	tkMessageBox.askyesno(title="Save",message="are you sure want to save this")
def mquit():
	mess = tkMessageBox.askyesno(title="Exit",message="are you sure want to quit")
	if mess == 1:
		mygui.destroy()
		ven.destroy() 
a = StringVar()
mygui.title("Phone Book")
ven.title("New contact ")

mygui.geometry("500x600+80+60")
ven.geometry("500x600+650+60")

myLabel1 = Label(text='Welcome to Contacts',fg = 'blue').pack()
myLabel2 = Button(text='New Contacts',fg = 'white',bg = 'blue',command = new).place(x = 50,y = 20)
myLabel3 = Button(text='view Contacts',fg = 'white',bg = 'blue',command = mnew).place(x = 50,y = 50)
myLabel4 = Button(text='Print Contacts',fg = 'white',bg = 'blue',command = mopen).place(x = 50,y = 80)

ven.text = Entry(textvariable = a).pack()

mymenu = Menu()
listone = Menu()
listone.add_command(label="New Contact",command = mnew)
listone.add_command(label="Open Contact",command = mopen)
listone.add_command(label="Save Contact",command = mbox)
listone.add_command(label="Exit Phonebook",command = mquit)

mymenu.add_cascade(label="File",menu=listone)
mymenu.add_cascade(label="Edit")
mymenu.add_cascade(label="Search")
mymenu.add_cascade(label="Help")
mygui.config(menu=mymenu)
mygui.mainloop()
ven.mainloop()
