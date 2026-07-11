from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QTableView, QHeaderView, QLineEdit, QPushButton
from PySide6.QtCore import QAbstractTableModel, Qt, QDate
from database import get_updates, add_update


# new
class update_model(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.rows = data

    def rowCount(self, parent=None):
        return len(self.rows)

    def columnCount(self, parent=None):
        return 3

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            row = index.row()
            col = index.column()
            return self.rows[row][col]
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                headers = ['ID', 'Note', 'Date']
                return headers[section]
        return None


class Update_table(QWidget):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        self.case_id = None
        self.setObjectName('table_widget')
        self.setStyleSheet('#table_widget {background-color:#2c2c2a; border:2px solid white; border-radius:12px;}')
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        #label row
        self.label_layout = QHBoxLayout()
        self.main_layout.addLayout(self.label_layout)

        self.label_details = QLabel('')
        self.label_details.setStyleSheet('font-size:15px; background-color:black;')
        self.client_label = QLabel('')
        self.label_layout.addWidget(self.label_details)
        self.label_layout.addStretch()
        self.label_layout.addWidget(self.client_label)

        # add update table view
        self.update_table = QTableView()
        self.update_table.setStyleSheet('background-color:black')
        self.update_table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.update_table.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignLeft)
        header = self.update_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.main_layout.addWidget(self.update_table)

        # add input row for adding new update
        self.input_layout = QHBoxLayout()
        self.main_layout.addLayout(self.input_layout)

        self.note_input = QLineEdit()
        self.note_input.setPlaceholderText('Type update note...')
        self.note_input.setStyleSheet('color:white; placeholder-text-color:#aaaaaa; background-color:#1a1a19;')
        self.input_layout.addWidget(self.note_input)

        self.add_btn = QPushButton('+ Add Update')
        self.add_btn.setStyleSheet('''
        QPushButton {color:white; background-color:#2a78d6;}
        QPushButton:hover {background-color:#1f5fad;}''')
        self.input_layout.addWidget(self.add_btn)

        self.add_btn.clicked.connect(self.save_update)

        # add hide until a case is selected
        self.hide()

    def show_case(self, row_data):
        self.case_id = row_data[0]
        self.label_details.setText(f'Case#{row_data[0]}.   {row_data[2]} | {row_data[3]}')
        self.label_details.setStyleSheet('font-size:15px')
        self.client_label.setText(f'{row_data[1]}')
        self.refresh_updates()
        self.show()

    # new
    def refresh_updates(self):
        data = get_updates(self.conn, self.case_id)
        self.model = update_model(data)
        self.update_table.setModel(self.model)

    # new
    def save_update(self):
        note = self.note_input.text()
        if not note or self.case_id is None:
            return
        date = QDate.currentDate().toString('MMMM d yyyy')
        add_update(self.conn, self.case_id, note, date)
        self.note_input.clear()
        self.refresh_updates()
