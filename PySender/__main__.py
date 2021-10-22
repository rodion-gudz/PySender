import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from PySender.ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()