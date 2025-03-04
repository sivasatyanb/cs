import sys;from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import os
import random
win1 = uic.loadUiType("Calendar04032025v1.ui")[0]

class CalendarScreen(QtWidgets.QMainWindow, win1):
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.startDate = ""
        self.endDate = ""
        self.today = QtCore.QDate.currentDate()
        self.numDays = 0
        self.output = ""
        self.CalStart.clicked[QtCore.QDate].connect(self.setStartDate)
        self.CalEnd.clicked[QtCore.QDate].connect(self.setEndDate)

    def setStartDate(self, date):
        self.lblStart.setText(" ")
        self.startDate = date

        if self.today < self.startDate:
            self.startDate = self.today
            self.lblStart.setText(self.today.toString())
        else:
            self.lblStart.setText(date.toString())
        self.lblStart.adjustSize()

    def setEndDate(self, date):
        self.lblEnd.setText(" ")
        self.endDate = date
        self.numDays = self.startDate.daysTo(self.endDate)
        if self.today > self.endDate:
            self.endDate = self.today
            if self.numDays > 0:
                self.output = "the number of days are ", self.numDays
            else:
                self.output = "invalid entry"
        else:
            self.output = "enter a date after than today"
        self.lblDays.setText(str(self.output))

app = QtWidgets.QApplication(sys.argv)
CalWindow = CalendarScreen(None)
CalWindow.show()
app.exec_()