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

# to fix:
# import sys;from PyQt5 import QtCore, QtGui, uic
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
# import os
# import random
# win1 = uic.loadUiType("Calendar11022025v2.ui")[0]

# class CalendarScreen(QtWidgets.QMainWindow, win1):
#     def __init__(self, parent = None):
#         QtWidgets.QMainWindow.__init__(self, parent)
#         self.setupUi(self);self.sDate="";self.eDate=""
#         self.CalStart.clicked[QtCore.QDate].connect(self.setSDate)
#         self.tDay=QtCore.QDate.currentDate();self.noDays=0
#         self.output=""
#         self.CalEnd.clicked[QtCore.QDate].connect(self.setEDate)
#     def setSDate(self,date):
#         self.lblStart.setText(" ");self.sDate=date
       
#         if self.tDay<self.sDate:
#             self.sDate=self.tDay
#             self.lblStart.setText(self.tDay.toString())
#             ##self.lblStart.setText("Not valid before current date")
#         else:
#             self.lblStart.setText(date.toString())
#         self.lblStart.adjustSize()
#     def setEDate(self,date):
#         self.lblEnd.setText(" ")
#         self.eDate=date;self.noDays=self.sDate.daysTo(self.eDate)
#         if self.tDay>self.eDate:
#             self.eDate=self.tDay
#             if self.noDays>0:
#                 self.output="the days are ",self.noDays
#             else:
#                 self.output="invalid entry"
#         else:
#             self.output="enter date greater than today"
#         self.lblDays.setText(str(self.output))
               
           
       
       
       
# app = QtWidgets.QApplication(sys.argv)
# CalWindow =CalendarScreen(None)
# CalWindow.show()
# app.exec_()