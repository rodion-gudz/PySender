import webbrowser

import PySender
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog

from PySender.ui.about import Ui_Dialog


def open_about_dialog():
    dialog = QDialog()
    dialog.ui = Ui_Dialog()
    dialog.ui.setupUi(dialog)
    dialog.ui.label_version.setText(PySender.__version__)
    dialog.ui.github_button.clicked.connect(lambda: webbrowser.open('https://github.com/fast-geek/PySender'))
    dialog.ui.pypi_button.clicked.connect(lambda: webbrowser.open('https://pypi.org/project/PySender'))
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    dialog.exec_()
