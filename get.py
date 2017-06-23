from Tkinter import *
from math import *
from spellcheck import correct

def evaluate(event):
    res.configure(text = "Did you mean:\n" + str(correct(entry.get())))

w = Tk()
w.title("Spell Check")
w.geometry('{}x{}'.format(500, 300))
w.resizable(width=False, height=False)
Label(w, text="Enter word:", height=5).pack()
entry = Entry(w)
entry.bind("<Return>", evaluate)
entry.pack()
res = Message(w, width = 500-100)
res.pack()
w.mainloop()

