from tkinter import *
from flask import Flask

app = Flask(__name__)

@app.routte("/")
def home():
        return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)

from tkinter import messagebox

window = Tk()


def displayinfo():
    messagebox.showinfo('Information for mood', 'Image; Song; Quote')


btnHappy = Button(window, text='Happy', fg='black', bg='#FFD700', command=displayinfo)
btnHappy.place(x=180, y=100)

btnSad = Button(window, text='Sad', fg='black', bg='#5F7C92', command=displayinfo)
btnSad.place(x=250, y=100)

btnAngry = Button(window, text='Angry', fg='black', bg='#AB2D2D', command=displayinfo)
btnAngry.place(x=300, y=100)

btnStressed = Button(window, text='Stressed', fg='black', bg='#874894', command=displayinfo)
btnStressed.place(x=365, y=100)

lbl = Label(window, text='Click on your current mood.', fg='black', font=("Times New Roman", 16))
lbl.place(x=180, y=50)

# txtfield = Entry(window, text='This is Entry Widget', bd=5)
# txtfield.place(x=225, y=150)

window.title('Hello Python')
window.geometry("600x200+25+25")
window.mainloop()