from tkinter import *

master = Tk()


def closewindow():
    exit()


button = Button(master, text="Close Window", comand=closewindow)

button.pack()

mainloop()