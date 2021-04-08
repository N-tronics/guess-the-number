"""
Provides functionality to btns in the __main__.py file.
"""

import json
import clsHS
from random import randint
from tkinter import messagebox


class Funcs:

    def __init__(self, ui, file='guess the number/high-scores.json'):
        self.main = ui
        self._jsonFile = file
        self._diff = 'not set'
        self._tries = 0
        self._difficulties = ['easyDifficulty', 'mediumDifficulty', 'hardDifficulty']

        self.findHighScorers()

    def findHighScorers(self):
        with open(self._jsonFile) as f:
            self._scores = json.load(f)

        easyHighScorer = list(self._scores['easyDifficulty'].keys())[0]
        mediumHighScorer = list(self._scores['mediumDifficulty'].keys())[0]
        hardHighScorer = list(self._scores['hardDifficulty'].keys())[0]

        eTries = self._scores['easyDifficulty'][easyHighScorer]
        mTries = self._scores['mediumDifficulty'][mediumHighScorer]
        hTries = self._scores['hardDifficulty'][hardHighScorer]

        return {easyHighScorer: eTries, mediumHighScorer: mTries, hardHighScorer: hTries}

    def showHighScorers(self):
        self.findHighScorers()
        self.main._ezyHS.set(list(self._scores['easyDifficulty'].keys()))
        self.main._medHS.set(list(self._scores['mediumDifficulty'].keys()))
        self.main._hardHS.set(list(self._scores['hardDifficulty'].keys()))

        self.main._eTries.set(list(self._scores['easyDifficulty'].values()))
        self.main._mTries.set(list(self._scores['mediumDifficulty'].values()))
        self.main._hTries.set(list(self._scores['hardDifficulty'].values()))

    def writeHighScorers(self, diff, score):
        with open(self._jsonFile) as f:
            storedData = json.load(f)

        storedData[diff] = score

        with open(self._jsonFile, 'w') as f:
            json.dump(storedData, f, indent=4)

        self.showHighScorers()

    def changeDiff(self):
        if self._diff != 'not set':
            response = messagebox.askokcancel('Do you want to continue?',
                                              'Proceeding will reset your tries and you will have to start over.')

            if response:
                self.reset()
            else:
                return
        else:
            return

    def setRandomNumber(self, diff):
        self.main.tries = 0
        self.main.disableButtons()

        if diff == 'e':
            self._diff = 'easyDifficulty'
            self._randomInt = randint(0, 10)
            self.main._selectedDiff.set('Difficulty: Easy')
            # print(self.main.randint)
        elif diff == 'm':
            self._diff = 'mediumDifficulty'
            self._randomInt = randint(0, 100)
            self.main._selectedDiff.set('Difficulty: Medium')
            # print(self.main.randint)
        else:
            self._diff = 'hardDifficulty'
            self._randomInt = randint(0, 500)
            self.main._selectedDiff.set('Difficulty: Hard')
            # print(self.main.randint)

    def verify(self, *args):
        num = self.main.getNum()
        name = self.main.getName()

        if name != '':
            if self._diff != 'not set':
                if num is not None:
                    try:
                        num = int(num)
                        self._tries += 1
                        self.main._tries.set('Tries: ' + str(self._tries))
                        self.evalEntry(num, name)
                        self.main.clearNumEntry()
                    except ValueError:
                        self.main._result.set('Please enter a number.')
                        self.main.clearNumEntry()
                else:
                    self.main._result.set('Please enter a number.')
            else:
                self.main._result.set('Please select a difficulty.')
        else:
            self.main._result.set('Please enter your name.')

    def evalEntry(self, num, name):
        hints = ['Too low, try again!', 'Too high, try again!', 'Almost there, try higher!', 'Almost there, try lower!']
        compliments = ['Great!', 'Awesome!', 'Superb!', 'Bravo!', 'Wow!', 'Amazing!']

        if num < self._randomInt:
            difference = abs(num - self._randomInt)
            if difference > 10:
                self.main._result.set(hints[0])
            elif difference <= 10:
                self.main._result.set(hints[2])
        elif num > self._randomInt:
            difference = abs(num - self._randomInt)
            if difference > 10:
                self.main._result.set(hints[1])
            elif difference <= 10:
                self.main._result.set(hints[3])
        else:
            messagebox.showinfo(compliments[randint(0, 5)],
                                'You got it right in ' + str(self._tries) + ' tries!')
            self.main.clearNumEntry()
            self.main.enableButtons()

            if list(self._scores[self._diff].values())[0] is None:
                self.writeHighScorers(self._diff, {name: self._tries})
                self.showHighScorers()
            elif self._tries < list(self._scores[self._diff].values())[0]:
                self.writeHighScorers(self._diff, {name: self._tries})
                self.showHighScorers()

                self._tries = 0
                self.main._tries.set('Tries: ' + str(self._tries))
                self._diff = 'not set'
                self.main._selectedDiff.set('Difficulty:')

            self.reset()
            self.showHighScorers()

    def launchClearHS(self):
        clsWindow = clsHS.Clear(self)
        clsWindow.winActivate()

    def clsHs(self):
        for diff in self._difficulties:
            self.writeHighScorers(diff, {'None': None})
        self._clearHighScores = False

        self.showHighScorers()
        self.reset()

    def reset(self):
        self._tries = 0
        self.main._tries.set('Tries: ' + str(self._tries))
        self.main._selectedDiff.set('Difficulty:')
        self.main._result.set('')
        self.main.clearNumEntry()
        self.main.enableButtons()
