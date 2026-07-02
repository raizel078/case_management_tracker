from PySide6.QtWidgets import QWidget , QVBoxLayout , QLabel
from control import controls
from case_table import all_cases_table
from PySide6.QtCore import Qt

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(700,600)
        self.setObjectName('MainWidget')
        self.setStyleSheet('#MainWidget {background-color:#0d0d0d;}')

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.title_label = QLabel('🗁 Case Management System')
        self.title_label.setStyleSheet('color:white; font-size:20px; font-weight:bold;')
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.main_layout.addWidget(self.title_label)

        self.control_widget = controls()
        self.main_layout.addWidget(self.control_widget)

        self.case_table = all_cases_table()
        self.main_layout.addWidget(self.case_table)






