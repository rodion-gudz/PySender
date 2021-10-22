import json
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from PySender.request import Request
from PySender.ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_send.clicked.connect(self.send_request)
        self.button_add.clicked.connect(self.add_header)
        self.delete_header_button.clicked.connect(self.remove_header)


    def send_request(self):
        request = Request(self.lineEdit_URL.text(), self.method_selector.currentText())
        request.send()
        self.field_response.setText(json.dumps(request.request.json(), indent=2, sort_keys=True))
        self.field_status_code.setText(str(request.request.status_code))

    def add_header(self):
        name = self.field_name.text()
        value = self.field_value.text()
        self.table_headers.setRowCount(self.table_headers.rowCount() + 1)
        self.table_headers.setItem(self.table_headers.rowCount() - 1, 0, QTableWidgetItem(name))
        self.table_headers.setItem(self.table_headers.rowCount() - 1, 1, QTableWidgetItem(value))

    def remove_header(self):
        self.table_headers.removeRow(self.table_headers.currentRow())



def main():
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
