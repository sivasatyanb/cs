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
            self.spinBox.setVisible(True)
        def sayit(self):
            myMessage=self.txtInput.text()
            if self.radio1.isChecked() == True:
                myMessage = 'gender is boy'
            elif self.radio2.isChecked() == True:
                myMessage = 'gender is girl'
            elif self.radio3.isChecked() == True:
                myMessage = 'gender is washing machine'
            else:
                myMessage='please enter something'
            self.lblOutput.setText(myMessage)
            self.txtInput.setText(" ")

app=QtWidgets.QApplication(sys.argv)  
w1=WindowClass(None)
w1.show()
app.exec_()