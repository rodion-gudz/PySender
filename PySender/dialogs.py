from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog

from PySender.ui.about import Ui_Dialog


def open_about_dialog():
    dialog = QDialog()
    dialog.ui = Ui_Dialog()
    dialog.ui.setupUi(dialog)
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    dialog.exec_()
