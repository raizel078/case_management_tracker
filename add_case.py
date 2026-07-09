from PySide6.QtWidgets import QDialog , QVBoxLayout , QLabel , QLineEdit , QHBoxLayout , QWidget , QComboBox ,QDateEdit , QPushButton
from PySide6.QtCore import Qt, QDate
from database import add_case , get_stats


class pop_up(QDialog):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        self.setWindowTitle('Add Case')
        self.setObjectName('pop')
        self.setStyleSheet('#pop {background-color:black;}')
        self.setFixedSize(300,250)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.client_label = QLabel('Client')
        self.client_label.setStyleSheet('color:white; font-size:15px; font-weight:bold')
        self.main_layout.addWidget(self.client_label)


        self.add_case_box = QLineEdit()
        self.add_case_box.setPlaceholderText('Type client name')
        self.add_case_box.setStyleSheet('color:white; placeholder-text-color:#aaaaaa; background-color:#1a1a19;')
        self.main_layout.addWidget(self.add_case_box)
        self.case_title_label = QLabel('Case Description')
        self.case_title_label.setStyleSheet('color:white; font-size:15px; font-weight:bold')
        self.main_layout.addWidget(self.case_title_label)


        self.case_title_box = QLineEdit()
        self.case_title_box.setPlaceholderText('eg. visa renewal delay')
        self.case_title_box.setStyleSheet('color:white; placeholder-text-color:#aaaaaa; background-color:#1a1a19;')
        self.main_layout.addWidget(self.case_title_box)
        self.status_date_row = QHBoxLayout()
        self.main_layout.addLayout(self.status_date_row)

        #open close combox widget
        self.status_widget = QWidget()
        self.status_date_row.addWidget(self.status_widget)
        self.open_layout = QVBoxLayout()
        self.status_widget.setLayout(self.open_layout)

        self.status_label = QLabel('Status')
        self.status_label.setStyleSheet('color:white; font-size:15px; font-weight:bold')
        self.open_layout.addWidget(self.status_label)

        self.status_choose = QComboBox()
        self.status_choose.addItems(['Open', 'Closed'])
        self.status_choose.setStyleSheet('color:white; background-color:#1a1a19; border:1px solid #333; border-radius:6px; padding:4px 8px;')
        self.open_layout.addWidget(self.status_choose)


        #another layout for the date part.
        self.date_widget =QWidget()
        self.status_date_row.addWidget(self.date_widget)
        self.date_layout = QVBoxLayout()
        self.date_widget.setLayout(self.date_layout)

        self.date_label = QLabel('Date')
        self.date_label.setStyleSheet('color:white; font-size:15px; font-weight:bold')
        self.date_layout.addWidget(self.date_label)

        self.date_picker = QDateEdit()
        self.date_picker.setCalendarPopup(True)
        self.date_picker.setDate(QDate.currentDate())
        self.date_picker.setStyleSheet('color:white; background-color:#1a1a19; border:1px solid #333; border-radius:6px; padding:4px 8px;')
        self.date_picker.setDisplayFormat('MMMM d yyyy')
        self.date_layout.addWidget(self.date_picker)
        self.main_layout.addStretch()

        #now save and cancel button.
        self.final_layout = QHBoxLayout()
        self.main_layout.addLayout(self.final_layout)

        #cancel button and it will cancel window.
        self.cancel_btn = QPushButton('Cancel')
        self.cancel_btn.setStyleSheet('''
        QPushButton {color:white;}
        QPushButton:hover {background-color:#ED0A02;}''')
        self.final_layout.addWidget(self.cancel_btn)

        self.cancel_btn.clicked.connect(self.reject)


        self.save_btn = QPushButton('Save')
        self.save_btn.setStyleSheet('''
        QPushButton {color:white; background-color:#2a78d6;}
        QPushButton:hover {background-color:#1f5fad;}''')
        self.final_layout.addWidget(self.save_btn)

        self.save_btn.clicked.connect(self.save_data)

    def save_data(self):
        client = self.add_case_box.text()
        title = self.case_title_box.text()
        status = self.status_choose.currentText()
        date = self.date_picker.text()

        add_case(self.conn, client, title, status, date)
        self.accept()

