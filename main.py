'''
GUI Guess the number V1
Nischay Bharadwaj
03-04-2021
'''

import json
from random import randint
from tkinter import *
from tkinter import messagebox

class GTNv1:
    def __init__(self):
        self.root = Tk()
        self.root.title('Guess the number! (v1)')
        self.root.resizable(False, False)

        self.gui()

    def gui(self):
        self.name = Entry(self.root, relief=RIDGE, borderwidth=5, width=42, bg='grey', fg='white')

        nameLbl = Label(self.root, text='Enter your name:')
        diffLbl = Label(self.root, text='Difficulty:', anchor='e', width=14)

        easyBtn = Button(self.root, text='Easy(0~10)', state=NORMAL)
        mediumBtn = Button(self.root, text='Medium(0~100)', state=NORMAL)
        hardBtn = Button(self.root, text='Hard(0~500)', state=NORMAL)

#       ===============================================================================================================

        self.name.grid(row=0, column=1, columnspan=3)

        nameLbl.grid(row=0, column=0)
        diffLbl.grid(row=1, column=0)

        easyBtn.grid(row=1, column=1)
        mediumBtn.grid(row=1, column=2)
        hardBtn.grid(row=1, column=3)

    def rootActivate(self):
        self.root.mainloop()


gtnv1 = GTNv1()
gtnv1.rootActivate()
