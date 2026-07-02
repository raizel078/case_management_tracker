from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView
from PySide6.QtCore import QAbstractTableModel, Qt

class all_cases_table(QWidget):
    def __init__(self):
        super().__init__()
        self.table = QTableView()