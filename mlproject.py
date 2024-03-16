import tkinter as tk
from tkinter import *
from tkinter import ttk
import os

win=tk.Tk()

win.title("Virtual Mouse")
win.geometry("300x220")

bg = PhotoImage(file='images.png')

label17 = Label(win, image=bg)

label17.place(x=40, y=0)

def hand():
    os.system("virtualmouse.py")
def handdetector():
    os.system("eyemouse.py")

button=ttk.Button(win,text="Virtual Mouse Using Hand",command=hand)
button2=ttk.Button(win,text="Virtual Mouse Using Eye",command=handdetector)
button.pack()
button2.pack()

win.mainloop()
