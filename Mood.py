from tkinter import *
import tkinter as tk

master = Tk()
root = tk.Tk()


def closewindow():
    exit()


def happy():
    print('Happy')


def sad():
    print('Sad')


def angry():
    print('Angry')


def stressed():
    print('Stressed')


label = tk.Label(root, text='Enter your current mood!')
label.grid(row=0, column=1)
label.pack()

button1 = Button(master, text="Happy", command=happy)
button1.grid(row=1, column=0)

button2 = Button(master, text="Sad", command=sad)
button2.grid(row=1, column=2)

button3 = Button(master, text="Angry", command=angry)
button3.grid(row=3, column=0)

button4 = Button(master, text="Stressed", command=stressed)
button4.grid(row=3, column=2)

root.mainloop()