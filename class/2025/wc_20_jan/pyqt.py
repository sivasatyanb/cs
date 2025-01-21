import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

window1 =uic.loadUiType("myui.ui")[0]

class WindowClass(QtWidgets.QMainWindow, window1):
        def __init__(self, parent=None): ## constructor
            QtWidgets.QMainWindow.__init__(self, parent)  ##
            self.setupUi(self)
            self.txtInput.setVisible(True)
            self.lblOutput.setVisible(True)
            self.btnOk.clicked.connect(self.sayit)
            self.radio1.setChecked(True)
        def sayit(self):
            myMessage=self.txtInput.text()
            if len(myMessage)>0:
                value = float(myMessage)
                if self.radio1.isChecked() == True:
                    result = value*1.61
                    myMessage ='the value in miles is: ' + str(result)
                elif self.radio2.isChecked() == True:
                    result = value/1.61
                    myMessage ='the value in miles is: ' + str(result)
            else:
                myMessage="please enter something"
            self.lblOutput.setText(myMessage);self.txtInput.setText(" ")

app=QtWidgets.QApplication(sys.argv)
w1=WindowClass(None)
w1.show()
app.exec_()