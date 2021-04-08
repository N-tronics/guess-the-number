"""
GUI Guess the number V1
Nischay Bharadwaj
03-04-2021
"""

import btnFuncs
from tkinter import *


class GTNv1:
    _root = Tk()
    _selectedDiff = StringVar()
    _tries = StringVar()
    _result = StringVar()
    _ezyHS = StringVar()
    _medHS = StringVar()
    _hardHS = StringVar()
    _eTries = StringVar()
    _mTries = StringVar()
    _hTries = StringVar()

    def __init__(self):
        jsonFile = '/home/nischay/documents/py/guess-the-number/guess the number/high-scores.json'
        self.btns = btnFuncs.Funcs(self, jsonFile)
        self._root.title('Guess the number! (v1)')
        self._root.resizable(False, False)

        self._selectedDiff.set('Difficulty:')
        self._tries.set('Tries: 0')

        self.ui()
        self.btns.showHighScorers()

    def ui(self):
        self.name = Entry(self._root, relief=RIDGE, borderwidth=5, width=42, bg='grey', fg='white')
        self.numIn = Entry(self._root, relief=RIDGE, borderwidth=5, width=25, bg='grey', fg='white')
        self.numIn.bind('<Return>', self.btns.verify)

        nameLbl = Label(self._root, text='Enter your name:')
        diffLbl = Label(self._root, text='Difficulty:', anchor='e', width=14)
        selectedDiffLbl = Label(self._root, textvariable=self._selectedDiff)
        triesLbl = Label(self._root, textvariable=self._tries)

        self.easyBtn = Button(self._root, text='Easy(0~10)', state=NORMAL,
                              command=lambda: self.btns.setRandomNumber('e'))
        self.mediumBtn = Button(self._root, text='Medium(0~100)', state=NORMAL,
                                command=lambda: self.btns.setRandomNumber('m'))
        self.hardBtn = Button(self._root, text='Hard(0~500)', state=NORMAL,
                              command=lambda: self.btns.setRandomNumber('h'))
        chkBtn = Button(self._root, text='Check', width=27, command=lambda: self.btns.verify())
        changeDiff = Button(self._root, text='Change Difficulty', command=lambda: self.btns.changeDiff())
        clsHS = Button(self._root, text='Clear High Scores', command=lambda: self.btns.launchClearHS())

        resultLbl = Label(self._root, textvariable=self._result)
        table_highScores = Label(self._root, text='High Scores:-', width=27, anchor='w')
        table_highScoresLbl = Label(self._root, text='High Scorer')
        table_triesLbl = Label(self._root, text='Tries')
        table_easyDiffLbl = Label(self._root, text='Easy Difficulty:', anchor='w', width=27)
        table_mediumDiffLbl = Label(self._root, text='Medium Difficulty:', anchor='w', width=27)
        table_hardDiffLbl = Label(self._root, text='Hard Difficulty:', anchor='w', width=27)
        table_ezyHighScorer = Label(self._root, textvariable=self._ezyHS)
        table_medHighScorer = Label(self._root, textvariable=self._medHS)
        table_hardHighScorer = Label(self._root, textvariable=self._hardHS)
        table_ezyTries = Label(self._root, textvariable=self._eTries)
        table_medTries = Label(self._root, textvariable=self._mTries)
        table_hardTries = Label(self._root, textvariable=self._hTries)

        #       ===============================================================================================================

        self.name.grid(row=0, column=1, columnspan=3)
        self.numIn.grid(row=2, column=0, columnspan=2)

        nameLbl.grid(row=0, column=0)
        diffLbl.grid(row=1, column=0)
        selectedDiffLbl.grid(row=3, column=0, columnspan=2)
        triesLbl.grid(row=3, column=2, columnspan=2)
        resultLbl.grid(row=4, column=0, columnspan=4)
        table_highScores.grid(row=5, column=0, columnspan=2)
        table_highScoresLbl.grid(row=5, column=2)
        table_triesLbl.grid(row=5, column=3)
        table_easyDiffLbl.grid(row=6, column=0, columnspan=2)
        table_mediumDiffLbl.grid(row=7, column=0, columnspan=2)
        table_hardDiffLbl.grid(row=8, column=0, columnspan=2)
        table_ezyHighScorer.grid(row=6, column=2)
        table_medHighScorer.grid(row=7, column=2)
        table_hardHighScorer.grid(row=8, column=2)
        table_ezyTries.grid(row=6, column=3)
        table_medTries.grid(row=7, column=3)
        table_hardTries.grid(row=8, column=3)

        self.easyBtn.grid(row=1, column=1)
        self.mediumBtn.grid(row=1, column=2)
        self.hardBtn.grid(row=1, column=3)
        chkBtn.grid(row=2, column=2, columnspan=2)
        changeDiff.grid(row=9, column=0, columnspan=2, pady=10)
        clsHS.grid(row=9, column=2, columnspan=2, pady=10)

    def disableButtons(self):
        self.easyBtn['state'] = DISABLED
        self.mediumBtn['state'] = DISABLED
        self.hardBtn['state'] = DISABLED

    def enableButtons(self):
        self.easyBtn['state'] = NORMAL
        self.mediumBtn['state'] = NORMAL
        self.hardBtn['state'] = NORMAL

    def clearNumEntry(self):
        self.numIn.delete(0, END)

    def rootActivate(self):
        self._root.mainloop()

    def getName(self):
        return self.name.get()

    def getNum(self):
        return self.numIn.get()


gtnv1 = GTNv1()
gtnv1.rootActivate()
