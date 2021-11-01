import json
import sys

import requests
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QDialog

from PySender.ui.about import Ui_Dialog
from PySender.ui.ui import Ui_MainWindow


def open_about():
    dialog = QDialog()
    dialog.ui = Ui_Dialog()
    dialog.ui.setupUi(dialog)
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    dialog.exec_()


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_send.clicked.connect(self.send_request)
        self.button_add.clicked.connect(self.add_header)
        self.delete_header_button.clicked.connect(self.remove_header)
        self.clear_button.clicked.connect(self.clear_headers)
        self.actionAbout.triggered.connect(open_about)
        self.lineEdit_URL.installEventFilter(self)

    def send_request(self):
        params = dict()
        for i in range(self.table_headers.rowCount()):
            params[self.table_headers.item(i, 0).text()] = self.table_headers.item(i, 1).text()
        try:
            request = getattr(requests, self.method_selector.currentText().lower()) \
                (self.lineEdit_URL.text(), **{"params" if self.method_selector.currentText() == "GET"
                                              else "data": params})
            self.field_response.setText(json.dumps(request.json(), indent=2, sort_keys=True))
            self.field_status_code.setText(str(request.status_code))
            self.tabWidget.setCurrentIndex(3)
        except requests.exceptions.MissingSchema:
            QMessageBox.warning(self, "Error", "Please enter a valid URL", QMessageBox.Ok)
        except json.decoder.JSONDecodeError:
            QMessageBox.information(self, "Error", "This site has no REST API", QMessageBox.Ok)

    def add_header(self):
        name = self.field_name.text().strip()
        value = self.field_value.text().strip()
        if "" in (name, value):
            QMessageBox.warning(self, "Error", "Please enter a valid header", QMessageBox.Ok)
        self.table_headers.setRowCount(self.table_headers.rowCount() + 1)
        self.table_headers.setItem(self.table_headers.rowCount() - 1, 0, QTableWidgetItem(name))
        self.table_headers.setItem(self.table_headers.rowCount() - 1, 1, QTableWidgetItem(value))
        self.field_name.setText("")
        self.field_value.setText("")

    def remove_header(self):
        if self.table_headers.currentRow() != -1:
            self.table_headers.removeRow(self.table_headers.currentRow())
        else:
            QMessageBox.warning(self, "Error", "Select the item you want to delete", QMessageBox.Ok)

    def clear_headers(self):
        self.table_headers.clearContents()
        self.table_headers.setRowCount(0)

    def eventFilter(self, obj, event):
        if (
                event.type() == QtCore.QEvent.KeyPress
                and obj is self.lineEdit_URL
                and event.key() == QtCore.Qt.Key_Return
                and self.lineEdit_URL.hasFocus()
        ):
            self.send_request()
        return super().eventFilter(obj, event)


def main():
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
