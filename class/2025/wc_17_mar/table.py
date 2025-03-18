import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
window1 = uic.loadUiType("class/2025/wc_17_mar/table.ui")[0]
import sqlite3 as lite
class WindowClass(QtWidgets.QMainWindow, window1):
        def __init__(self, parent=None):
            QtWidgets.QMainWindow.__init__(self, parent)
            self.setupUi(self)
            self.tblNames.setColumnWidth(0,200)
            self.tblNames.setColumnWidth(1,200)
            self.tblNames.setColumnWidth(2,150)
            self.loadData()
        def loadData(self):
            self.tblNames.setHorizontal(["PupilId","FullName","RegGroup"])
            con = lite.connect("class/2025/wc_17_mar/database.db");cur = con.cursor()
            Records="""select Boys.PupilId, Boys.FullName, Boys.RegGroup
            from Boys
"""
            cur.execute(Records);results=cur.fetchall()
            row=0
            self.tblNames.setRowCount(len(results));
            for eachPerson in results:
               self.tblNames.setItem(row,0,QtWidgets.QTableWidgetItem(eachPerson[0]))
               self.tblNames.setItem(row,1,QtWidgets.QTableWidgetItem(eachPerson[1]))
               self.tblNames.setItem(row,2,QtWidgets.QTableWidgetItem(eachPerson[2]))
               row+=1
        def select(self,curr):
            self.lblOutput.setText(curr.data())
            row=curr.row()
            self.lblOutput.resize(self.lblOutput.sizeHint())
           
               
app = QtWidgets.QApplication(sys.argv)
w1 = WindowClass(None)
w1.show()
app.exec_()