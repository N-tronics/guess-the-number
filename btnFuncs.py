'''
Provides functionality to btns in the __main__.py file.
'''

import json
import __main__
from random import randint
from tkinter import *
from tkinter import messagebox

class funcs:
    def __init__(self, file, mainUi):
        self.main = mainUi
        self._jsonFile = file

    def findHighScorers(self):
        with open(self._jsonFile) as f:
            scores = json.load(f)

        easyHighScorer = list(scores['easyDifficulty'].keys())[0]
        mediumHighScorer = list(scores['mediumDifficulty'].keys())[0]
        hardHighScorer = list(scores['hardDifficulty'].keys())[0]

        eTries = scores['easyDifficulty'][easyHighScorer]
        mTries = scores['mediumDifficulty'][mediumHighScorer]
        hTries = scores['hardDifficulty'][hardHighScorer]

        return {easyHighScorer:eTries, mediumHighScorer:mTries, hardHighScorer:hTries}

    def showHighScorers(self):
        highScores = self.findHighScorers()

        self.main._ezyHS.set(list(highScores.keys())[0])
        self.main._medHS.set(list(highScores.keys())[1])
        self.main._hardHS.set(list(highScores.keys())[2])

        self.main._eTries.set(list(highScores.values())[0])
        self.main._mTries.set(list(highScores.values())[1])
        self.main._hTries.set(list(highScores.values())[2])

    def writeHighScorers(self, diff, score):
        with open(self._jsonFile) as f:
            storedData = json.load(f)

        storedData[diff] = score

        with open(self._jsonFile, 'w') as f:
            json.dump(storedData, f, indent=4)

        self.showHighScorers()

    def changeDiff(self):
        response = messagebox.askokcancel('Do you want to continue?',
                                          'Proceeding will reset your tries and you will have to start over.')

        if response:
            self._diff = 'not set'
            self._tries = 0
            self.main._tries = ('Tries:', self._tries)
            self.main._selectedDiff.set('Difficulty: ')
            self.main.clearNumEntry()
            self.main.enableBtns()
            self.main._rslt.set('')
        else:
            return

    def setRandomNumber(self, diff):
        self.main.tries = 0
        self.main.disableBtns()

        if diff == 'e':
            self._diff = 'easyDifficulty'
            self.main._randomInt = randint(0, 10)
            self.main._selectedDiff.set('Difficulty: Easy')
            #print(self.main.randint)
        elif diff == 'm':
            self._diff = 'mediumDifficulty'
            self.main._randomInt = randint(0, 100)
            self.main._selectedDiff.set('Difficulty: Medium')
            #print(self.main.randint)
        else:
            self._diff = 'hardDifficulty'
            self.main._randomInt = randint(0, 500)
            self.main._selectedDiff.set('Difficulty: Hard')
            #print(self.main.randint)

