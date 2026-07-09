import sys
from PySide6.QtWidgets import QApplication
from ui import MainWidget
from database import create_table , create_connection

if __name__=='__main__':
    app = QApplication(sys.argv)
    conn = create_connection()
    create_table(conn)
    window = MainWidget(conn)
    window.show()
    sys.exit(app.exec())