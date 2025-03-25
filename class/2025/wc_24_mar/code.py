import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Tables in PyQT5 :)')
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.table = QTableWidget(3, 3)
        self.table.setHorizontalHeaderLabels(['Darren', 'Derek', 'Dylan'])
        self.table.setVerticalHeaderLabels(['Row 1', 'Row 2', 'Row 3'])
        self.populate_table()
        self.layout.addWidget(self.table)

        self.input_layout = QHBoxLayout()
        self.text_field = QLineEdit()
        self.text_field.setPlaceholderText('Enter value for new row')
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.add_row)

        self.input_layout.addWidget(self.text_field)
        self.input_layout.addWidget(self.submit_button)
        self.layout.addLayout(self.input_layout)

    def populate_table(self):
        data = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(value))

    def add_row(self):
        value = self.text_field.text()
        if value:
            current_row_count = self.table.rowCount()
            self.table.insertRow(current_row_count)
            self.table.setItem(current_row_count, 0, QTableWidgetItem(value))
            self.text_field.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())