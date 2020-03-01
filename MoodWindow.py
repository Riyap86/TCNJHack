from tkinter import *
from tkinter import messagebox

window = Tk()


def displayinfo():
    messagebox.showinfo('Information for mood', 'Image; Song; Movie')


def closewindow():
    exit()


btnHappy = Button(window, text='Happy', fg='black', bg='#FFD700', command=displayinfo)
btnHappy.place(x=180, y=100)

btnSad = Button(window, text='Sad', fg='black', bg='#5F7C92', command=displayinfo)
btnSad.place(x=250, y=100)

btnAngry = Button(window, text='Angry', fg='black', bg='#AB2D2D', command=displayinfo)
btnAngry.place(x=300, y=100)

btnStressed = Button(window, text='Stressed', fg='black', bg='#874894', command=displayinfo)
btnStressed.place(x=365, y=100)

btnExit = Button(window, text='Exit Page', fg='black', bg='grey', command=closewindow)
btnExit.place(x=275, y=150)

lbl = Label(window, text='Click on your current mood.', fg='black', font=("Times New Roman", 16))
lbl.place(x=180, y=50)

# txtfield = Entry(window, text='This is Entry Widget', bd=5)
# txtfield.place(x=225, y=150)

window.title('Hello Python')
window.geometry("600x200+25+25")
window.mainloop()