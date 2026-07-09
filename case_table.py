from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView, QHeaderView, QHBoxLayout, QLineEdit, QComboBox
from PySide6.QtCore import QAbstractTableModel, Qt
from database import get_cases


class case_model(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.rows = data

    def rowCount(self, parent=None):
        return len(self.rows)

    def columnCount(self, parent=None):
        return 5

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            row = index.row()
            col = index.column()
            return self.rows[row][col]
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                headers = ['ID', 'Client', 'Case title', 'Status', 'Updates']
                return headers[section]
        return None


class all_cases_table(QWidget):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        self.data = get_cases(self.conn)
        self.model = case_model(self.data)
        self.table_layout = QVBoxLayout()
        self.setLayout(self.table_layout)   # only ONE setLayout on this widget
        self.table = QTableView()
        self.table.setModel(self.model)

        # now search bar and All statuses
        # CHANGED: build the search row, then add it into table_layout ABOVE the table
        self.search_layout = QHBoxLayout()
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText('\U0001F50D\uFE0E Search By client or title ')
        self.search_bar.setStyleSheet('color:white; placeholder-text-color:#aaaaaa; background-color:#1a1a19;')
        self.search_layout.addWidget(self.search_bar)
        # not all status
        self.status = QComboBox()
        self.status.addItems(['All status', 'Open', 'Closed'])
        self.status.setStyleSheet('background-color:#2a78d6;')
        self.search_layout.addWidget(self.status)
        # ADDED: search row into the main layout (search above, table below)
        self.table_layout.addLayout(self.search_layout)

        # ADDED: table goes in after the search row
        self.table_layout.addWidget(self.table)

        # styling the header and adjusting it.
        self.table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.table.setStyleSheet('background-color:black')
        self.table.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignLeft)
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)

