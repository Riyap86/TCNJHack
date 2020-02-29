from tkinter import *

master = Tk()


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


print('How are you feeling today?')


button1 = Button(master, text="Close Window", command=closewindow)
button1.grid(row=7, column=1)

button2 = Button(master, text="Happy", command=happy)
button2.grid(row=0, column=0)

button3 = Button(master, text="Sad", command=sad)
button3.grid(row=0, column=2)

button4 = Button(master, text="Angry", command=angry)
button4.grid(row=2, column=0)

button5 = Button(master, text="Stressed", command=stressed)
button5.grid(row=2, column=2)

mainloop()