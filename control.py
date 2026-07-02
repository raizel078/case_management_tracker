from tkinter import dialog

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget , QVBoxLayout , QLabel , QHBoxLayout , QPushButton , QLineEdit , QComboBox
from add_case import pop_up



class controls(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName('controls')
        self.setStyleSheet('#controls {background-color:black;}')

        self.control_main = QVBoxLayout()
        self.setLayout(self.control_main)

        #all case and add button.
        self.first_layout = QHBoxLayout()
        self.control_main.addLayout(self.first_layout)
        self.all_case_title = QLabel('All Cases')
        self.all_case_title.setStyleSheet('color:white; font-size:15px; font-weight:bold')
        self.first_layout.addWidget(self.all_case_title)

        #add case bottom
        self.add_bottom = QPushButton('+ Add Case')
        self.add_bottom.setFixedWidth(100)
        self.add_bottom.setStyleSheet('''
        QPushButton {color:white; background-color:#2a78d6;}
        QPushButton:hover {background-color:#1f5fad;}''')
        self.first_layout.addWidget(self.add_bottom)


        #stat card
        self.stats_layout = QHBoxLayout()
        self.control_main.addLayout(self.stats_layout)
        self.total_case = self.create_stats('Total Case','0','#f5f5f5' )
        self.open_case = self.create_stats('Open case', '0','#db9300')
        self.close_case = self.create_stats('Close case', '0','#0ca30c')

        self.stats_layout.addWidget(self.total_case)
        self.stats_layout.addWidget(self.open_case)
        self.stats_layout.addWidget(self.close_case)


        #now search bar and All statuses
        self.search_layout = QHBoxLayout()
        self.control_main.addLayout(self.search_layout)
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText('🔍︎ Search By client or title ')
        self.search_layout.addWidget(self.search_bar)
        self.search_bar.setStyleSheet('color:white; placeholder-text-color:#aaaaaa; background-color:#1a1a19;')
        self.control_main.addStretch()

        #not all status
        self.status = QComboBox()
        self.status.addItems(['All status', 'Open', 'Closed'])
        self.status.setStyleSheet('background-color:#2a78d6;')
        self.search_layout.addWidget(self.status)

        self.add_bottom.clicked.connect(self.open_dialog)

    def open_dialog(self):
        dialog = pop_up()
        dialog.exec()


    def create_stats(self, title_text, value_text, color):
        box = QWidget()
        box.setStyleSheet('background-color:#1a1a19; border-radius: 10px;')
        box_layout = QVBoxLayout()
        box.setLayout(box_layout)
        title = QLabel(title_text)
        title.setStyleSheet('color:white; font-size:13px; font-weight:bold;')
        value = QLabel(value_text)
        value.setStyleSheet(f'font-size:20px; color:{color}')

        box_layout.addWidget(title)
        box_layout.addWidget(value)
        return box






