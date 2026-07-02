from PySide6.QtWidgets import QDialog , QVBoxLayout , QLabel , QLineEdit , QHBoxLayout , QWidget
class pop_up(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Case')
        self.setObjectName('pop')
        self.setStyleSheet('#pop {background-color:black;}')
        self.setFixedSize(300,400)

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


        #another layout for the date part.
        self.date_widget =QWidget()
        self.status_date_row.addWidget(self.date_widget)
        self.main_layout.addStretch()