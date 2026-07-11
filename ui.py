from PySide6.QtWidgets import QWidget , QVBoxLayout , QLabel
from control import controls
from case_table import all_cases_table
from add_case import pop_up
from PySide6.QtCore import Qt
from update_panel import Update_table

class MainWidget(QWidget):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        self.setMinimumSize(700,600)
        self.setObjectName('MainWidget')
        self.setStyleSheet('#MainWidget {background-color:#0d0d0d;}')

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.title_label = QLabel('🗁 Case Management System')
        self.title_label.setStyleSheet('color:white; font-size:20px; font-weight:bold;')
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.main_layout.addWidget(self.title_label)
        #control file connected here
        self.control_widget = controls(self.conn)
        self.main_layout.addWidget(self.control_widget)
        #all cases file connected here
        self.case_table = all_cases_table(conn)
        self.main_layout.addWidget(self.case_table)

        #new update file connected here.
        self.update_table = Update_table(self.conn) # modified
        self.main_layout.addWidget(self.update_table)
        #clicked to open the update panel.
        self.case_table.case_selected.connect(self.update_table.show_case)

        self.main_layout.addStretch()
        #signal catch and open pop_up.
        self.control_widget.add_clicked.connect(self.open_dialog)

    def open_dialog(self):
        dialog = pop_up(self.conn)
        dialog.exec()
        self.control_widget.refresh_stats()
        self.case_table.refresh_table()






