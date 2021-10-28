import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.build.ui import Ui_MainWindow

app = QApplication(sys.argv)

window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

window.show()

ui.main_window_status.setStyleSheet("color:#ff0011;")
ui.current_project_title.setText("Testing123")
ui.main_window_status.setText("Failing")

app.exec()