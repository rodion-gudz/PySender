# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.2.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 854)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_method = QtWidgets.QLabel(self.centralwidget)
        self.label_method.setObjectName("label_method")
        self.horizontalLayout_3.addWidget(self.label_method)
        self.method_selector = QtWidgets.QComboBox(self.centralwidget)
        self.method_selector.setObjectName("method_selector")
        self.method_selector.addItem("")
        self.method_selector.addItem("")
        self.method_selector.addItem("")
        self.method_selector.addItem("")
        self.method_selector.addItem("")
        self.horizontalLayout_3.addWidget(self.method_selector)
        self.field_URL = QtWidgets.QLabel(self.centralwidget)
        self.field_URL.setObjectName("field_URL")
        self.horizontalLayout_3.addWidget(self.field_URL)
        self.lineEdit_URL = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_URL.setObjectName("lineEdit_URL")
        self.horizontalLayout_3.addWidget(self.lineEdit_URL)
        self.button_send = QtWidgets.QPushButton(self.centralwidget)
        self.button_send.setObjectName("button_send")
        self.horizontalLayout_3.addWidget(self.button_send)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("font: 18pt;")
        self.label_3.setObjectName("label_3")
        # self.verticalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_username = QtWidgets.QLabel(self.widget)
        self.label_username.setObjectName("label_username")
        # self.horizontalLayout_5.addWidget(self.label_username, 0, QtCore.Qt.AlignTop)
        self.field_username = QtWidgets.QLineEdit(self.widget)
        self.field_username.setObjectName("field_username")
        # self.horizontalLayout_5.addWidget(self.field_username, 0, QtCore.Qt.AlignTop)
        self.label_password = QtWidgets.QLabel(self.widget)
        self.label_password.setObjectName("label_password")
        # self.horizontalLayout_5.addWidget(self.label_password, 0, QtCore.Qt.Top)
        self.field_password = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.field_password.sizePolicy().hasHeightForWidth())
        self.field_password.setSizePolicy(sizePolicy)
        self.field_password.setObjectName("field_password")
        # self.horizontalLayout_5.addWidget(self.field_password, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 100)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.widget, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_9)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_headers = QtWidgets.QLabel(self.tab_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_headers.sizePolicy().hasHeightForWidth())
        self.label_headers.setSizePolicy(sizePolicy)
        self.label_headers.setStyleSheet("font: 18pt;")
        self.label_headers.setObjectName("label_headers")
        # self.verticalLayout_3.addWidget(self.label_headers, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_name = QtWidgets.QLabel(self.tab_9)
        self.label_name.setObjectName("label_name")
        # self.horizontalLayout_7.addWidget(self.label_name, 0, QtCore.Qt.AlignTop)
        self.field_name = QtWidgets.QLineEdit(self.tab_9)
        self.field_name.setObjectName("field_name")
        # self.horizontalLayout_7.addWidget(self.field_name, 0, QtCore.Qt.AlignTop)
        self.label_value = QtWidgets.QLabel(self.tab_9)
        self.label_value.setObjectName("label_value")
        # self.horizontalLayout_7.addWidget(self.label_value, 0, QtCore.Qt.AlignTop)
        self.field_value = QtWidgets.QLineEdit(self.tab_9)
        self.field_value.setObjectName("field_value")
        # self.horizontalLayout_7.addWidget(self.field_value, 0, QtCore.Qt.AlignTop)
        self.button_add = QtWidgets.QPushButton(self.tab_9)
        self.button_add.setObjectName("button_add")
        # self.horizontalLayout_7.addWidget(self.button_add, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.table_headers = QtWidgets.QTableWidget(self.tab_9)
        self.table_headers.setObjectName("table_headers")
        self.table_headers.setColumnCount(2)
        self.table_headers.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_headers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_headers.setHorizontalHeaderItem(1, item)
        self.verticalLayout_3.addWidget(self.table_headers)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_3.setObjectName("pushButton_3")
        # self.verticalLayout_3.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab_10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_body = QtWidgets.QLabel(self.tab_10)
        self.label_body.setStyleSheet("font: 18pt;")
        self.label_body.setObjectName("label_body")
        self.verticalLayout_4.addWidget(self.label_body)
        self.field_body = QtWidgets.QTextEdit(self.tab_10)
        self.field_body.setObjectName("field_body")
        self.verticalLayout_4.addWidget(self.field_body)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab_10, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.tab_8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_response = QtWidgets.QLabel(self.tab_8)
        self.label_response.setStyleSheet("font: 18pt;")
        self.label_response.setObjectName("label_response")
        self.verticalLayout_5.addWidget(self.label_response)
        self.field_response = QtWidgets.QTextEdit(self.tab_8)
        self.field_response.setObjectName("field_response")
        self.verticalLayout_5.addWidget(self.field_response)
        self.horizontalLayout_9.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.tab_8, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1115, 24))
        self.menubar.setObjectName("menubar")
        self.menuProgram = QtWidgets.QMenu(self.menubar)
        self.menuProgram.setObjectName("menuProgram")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSupport = QtGui.QAction(MainWindow)
        self.actionSupport.setObjectName("actionSupport")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuProgram.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionSupport)
        self.menubar.addAction(self.menuProgram.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PySender"))
        self.label_method.setText(_translate("MainWindow", "Method"))
        self.method_selector.setItemText(0, _translate("MainWindow", "GET"))
        self.method_selector.setItemText(1, _translate("MainWindow", "POST"))
        self.method_selector.setItemText(2, _translate("MainWindow", "PUT"))
        self.method_selector.setItemText(3, _translate("MainWindow", "PATCH"))
        self.method_selector.setItemText(4, _translate("MainWindow", "DELETE"))
        self.field_URL.setText(_translate("MainWindow", "URL"))
        self.button_send.setText(_translate("MainWindow", "Send"))
        self.label_3.setText(_translate("MainWindow", "Basic authentication "))
        self.label_username.setText(_translate("MainWindow", "Username"))
        self.label_password.setText(_translate("MainWindow", "Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "Authentication"))
        self.label_headers.setText(_translate("MainWindow", "Headers"))
        self.label_name.setText(_translate("MainWindow", "Name"))
        self.label_value.setText(_translate("MainWindow", "Value"))
        self.button_add.setText(_translate("MainWindow", "Add"))
        self.table_headers.setSortingEnabled(True)
        item = self.table_headers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table_headers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Headers"))
        self.label_body.setText(_translate("MainWindow", "Body"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("MainWindow", "Body"))
        self.label_response.setText(_translate("MainWindow", "Response"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "Response"))
        self.menuProgram.setTitle(_translate("MainWindow", "Program"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionSupport.setText(_translate("MainWindow", "Support"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
