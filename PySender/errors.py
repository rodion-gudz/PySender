from PyQt5.QtWidgets import QMessageBox


class IncorrectRequest(Exception):
    pass


class NoSelectedRow(Exception):
    pass