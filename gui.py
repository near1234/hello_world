from tkinter import *

i = 0


def increment():
    global i
    i = i + 1
    Label1.config(text=i)


master = Tk()
Label1 = Label(master, text="0")
Button1 = Button(master, text="Benjamin Button", command=increment)
Button1.pack()
Label1.pack()
mainloop()
