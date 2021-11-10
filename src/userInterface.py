# this file will set up the user interface and bind it to the back end
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.build.ui import Ui_MainWindow
from src.UserInterfaceController.mainWindowController import UserInterfaceController


class UserInterface:
    def __init__(self, _args):
        self.m_ui = Ui_MainWindow()
        self.m_qt_app = QApplication(_args)
        self.m_qt_window = QMainWindow()
        self.m_uic_controller = None

    def __bind__(self):
        self.m_ui.buttonArray_no_0.clicked.connect(self.m_uic_controller.no_0_wrapper)
        self.m_ui.buttonArray_no_1.clicked.connect(self.m_uic_controller.no_1_wrapper)
        self.m_ui.buttonArray_no_2.clicked.connect(self.m_uic_controller.no_2_wrapper)
        self.m_ui.buttonArray_no_3.clicked.connect(self.m_uic_controller.no_3_wrapper)
        self.m_ui.buttonArray_no_4.clicked.connect(self.m_uic_controller.no_4_wrapper)
        self.m_ui.buttonArray_no_5.clicked.connect(self.m_uic_controller.no_5_wrapper)
        self.m_ui.buttonArray_no_6.clicked.connect(self.m_uic_controller.no_6_wrapper)
        self.m_ui.buttonArray_no_7.clicked.connect(self.m_uic_controller.no_7_wrapper)
        self.m_ui.buttonArray_no_8.clicked.connect(self.m_uic_controller.no_8_wrapper)
        self.m_ui.buttonArray_no_9.clicked.connect(self.m_uic_controller.no_9_wrapper)

        self.m_ui.buttonArray_op_dec.clicked.connect(self.m_uic_controller.dec_wrapper)
        self.m_ui.buttonArray_op_neg.clicked.connect(self.m_uic_controller.sign_wrapper)

    def initialize(self):
        self.m_ui.setupUi(self.m_qt_window)
        self.m_uic_controller = UserInterfaceController(self.m_ui.outputDisplay)
        self.__bind__()

    def run(self):
        self.m_qt_window.show()
        return self.m_qt_app.exec()
