"""
Launches a window to clear the high scores.
"""

from tkinter import *
from tkinter import messagebox


class Clear:
    def __init__(self, funcs):
        self.funcs = funcs
        self.clsWin = Tk()
        self.clsWin.title('Enter password to clear the high scores')
        self.clsWin.resizable(False, False)

        self.correctPwd = 'clshs'
        self.ui()

    def ui(self):
        """
        Generates the UI for entering the password.\n
        :return: None
        """
        pwdLbl = Label(self.clsWin, text='Password:')
        self.pwd = Entry(self.clsWin, borderwidth=5, relief=RIDGE, width=40)
        self.pwd.bind('<Return>', self.chkPwd)

        #       ========================================================================================

        pwdLbl.grid(row=0, column=0),
        self.pwd.grid(row=0, column=1)

    def chkPwd(self, *args):
        """
        Checks the password.\n
        :param args: event
        :return: None
        """
        if self.pwd.get() == self.correctPwd:
            self.clsWin.destroy()
            self.funcs.clsHs()
        else:
            messagebox.showerror('Invalid Password!', 'You entered an invalid password.')
            self.clsWin.destroy()

    def winActivate(self):
        """
        Keeps the password UI in a loop.\n
        :return: None
        """
        self.clsWin.mainloop()
