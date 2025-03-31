import sys
from PyQt5.QtWidgets import QApplication, QTableView, QVBoxLayout, QWidget, QFileDialog, QPushButton
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import sqlite3

class BlankTable(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 400)

        self.openfilebutton = QPushButton("Choose File")
        self.openfilebutton.clicked.connect(self.openfilepressed)

        self.table = QTableView()
        self.model = QStandardItemModel()
        self.table.setModel(self.model)

        layout = QVBoxLayout()
        layout.addWidget(self.openfilebutton)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def openfilepressed(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Open Database File", "",
                                                  "SQLite Database (*.db);;All Files (*)")
        if filepath:
            self.loadData(filepath)

    def loadData(self, filepath):
        conn = sqlite3.connect(filepath)
        cursor = conn.cursor()

        cursor.execute("PRAGMA table_info(Boys)")
        columns = [col[1] for col in cursor.fetchall()]  
        column_count = len(columns)

        if column_count == 0:
            print("No columns found in the table.")
            return

        self.model.setColumnCount(column_count)
        self.model.setHorizontalHeaderLabels(columns)

        cursor.execute(f"SELECT * FROM Boys")
        rows = cursor.fetchall()
        conn.close()

        self.model.setRowCount(0)

        for row_data in rows:
            items = [QStandardItem(str(item)) for item in row_data]
            self.model.appendRow(items)

app = QApplication(sys.argv)
window = BlankTable()
window.show()
sys.exit(app.exec_())