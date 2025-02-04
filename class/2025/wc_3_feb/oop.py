import sys;from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import os
import random
win1 = uic.loadUiType("calendar.ui")[0]

class CalendarScreen(QtWidgets.QMainWindow, win1):
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self);self.sDate="";self.eDate=""
        self.calendar1.clicked[QtCore.QDate].connect(self.setSDate)
       
    def setSDate(self,date):
        self.label.setText(" ")
        self.sDate=date
        self.label.setText(date.toString())
        self.label.adjustSize()
       
app = QtWidgets.QApplication(sys.argv)
CalWindow =CalendarScreen(None)
CalWindow.show()
app.exec_()