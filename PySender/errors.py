from PyQt5.QtWidgets import QMessageBox


def valid_url(self):
    QMessageBox.warning(self, "Error", "Please enter a valid URL", QMessageBox.Ok)


def json_error(self):
    QMessageBox.information(self, "Error", "This site has no REST API", QMessageBox.Ok)


def empty_request(self):
    QMessageBox.information(self, "Error", "Please send a request first", QMessageBox.Ok)
