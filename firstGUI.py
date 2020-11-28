#!/usr/bin/python3
from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=30,borderwidth=5)
e.grid(row=0, column=0,columnspan=3,padx=10,pady=10)
#e.insert(0,"enter your name: ")
def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
def button_clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)

    if math == 'addition':
        e.insert(int(0),f_num + int(second_number))
    if math == 'subtraction':
        e.insert(int(0),f_num - int(second_number))
    if math == 'multiplication':
        e.insert(int(0),f_num * int(second_number))
    if math == 'division':
        e.insert(int(0),f_num / int(second_number))


def button_subtract():
        first_number = e.get()
        global f_num
        global math
        math = 'subtraction'
        f_num = int(first_number)
        e.delete(0,END)

def button_multiply():
        first_number = e.get()
        global f_num
        global math
        math = 'multiplication'
        f_num = int(first_number)
        e.delete(0,END)

def button_divide():
        first_number = e.get()
        global f_num
        global math
        math = 'division'
        f_num = int(first_number)
        e.delete(0,END)

button_1 = Button(root, text="1",padx=40,pady=20,command=lambda: button_click(1))
button_2 = Button(root, text="2",padx=40,pady=20,command=lambda: button_click(2))
button_3 = Button(root, text="3",padx=40,pady=20,command=lambda: button_click(3))
button_4 = Button(root, text="4",padx=40,pady=20,command=lambda: button_click(4))
button_5 = Button(root, text="5",padx=40,pady=20,command=lambda: button_click(5))
button_6 = Button(root, text="6",padx=40,pady=20,command=lambda: button_click(6))
button_7 = Button(root, text="7",padx=40,pady=20,command=lambda: button_click(7))
button_8 = Button(root, text="8",padx=40,pady=20,command=lambda: button_click(8))
button_9 = Button(root, text="9",padx=40,pady=20,command=lambda: button_click(9))
button_0 = Button(root, text="0",padx=40,pady=20,command=lambda: button_click(0))
button_add = Button(root, text="+",padx=39,pady=20,command=button_add)
button_equal = Button(root, text="=",padx=89,pady=20,command=button_equal)
button_clear = Button(root, text="Clear",padx=79,pady=20,command=button_clear)

button_subtract = Button(root, text="-",padx=42,pady=20,command=button_subtract)
button_multiply = Button(root, text="*",padx=41,pady=20,command=button_multiply)
button_divide = Button(root, text="/",padx=41,pady=20,command=button_divide)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)

button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

#myButton = Button(root, text="Enter your name", command = myClick, fg='blue', bg='red')
#myButton.grid(column=1, row=0)



root.mainloop()
#########################################################
# myLabel1 = Label(root, text="Hello World")
# myLabel2 = Label(root, text="My name is John Elder")
# #myLabel.pack()
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=1)
############################################################1
# import tkinter as tk
# import tkinter as ttk
#
# win = tk.Tk()
# win.title("Witaj piracie")
# #win.resizable(0,0)
# #ttk.Label(win,text='Labelowy tekscik').grid(column=0, row=0)
#
# aLabel = ttk.Label(win, text='TATA')
# aLabel.grid(column=0, row=0)
# aLabel1 = ttk.Label(win, text='MAMA')
# aLabel1.grid(column=0, row=1)
#
# def clickMe():
#     action.configure(text="zmiana banana")
#     aLabel.configure(foreground='red')
#     aLabel.configure(text='ARMATA')
#
# def clickMe1():
#     action1.configure(text="zmiana banana")
#     aLabel1.configure(foreground='red')
#     aLabel1.configure(text='SMIETANA')
#
# action = ttk.Button(win, text='kliknij mnie', command=clickMe)
# action.grid(column=1,row=0)
#
# action1 = ttk.Button(win, text='kliknij mnie', command=clickMe1)
# action1.grid(column=1,row=1)
#
# win.mainloop()
