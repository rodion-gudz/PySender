# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 884)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("font: 18pt;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_13.addWidget(self.label)
        self.auth_typ_cbox = QtWidgets.QComboBox(self.widget)
        self.auth_typ_cbox.setObjectName("auth_typ_cbox")
        self.auth_typ_cbox.addItem("")
        self.auth_typ_cbox.addItem("")
        self.horizontalLayout_13.addWidget(self.auth_typ_cbox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_username = QtWidgets.QLabel(self.widget)
        self.label_username.setObjectName("label_username")
        self.horizontalLayout_5.addWidget(self.label_username, 0, QtCore.Qt.AlignTop)
        self.field_username = QtWidgets.QLineEdit(self.widget)
        self.field_username.setObjectName("field_username")
        self.horizontalLayout_5.addWidget(self.field_username, 0, QtCore.Qt.AlignTop)
        self.label_password = QtWidgets.QLabel(self.widget)
        self.label_password.setObjectName("label_password")
        self.horizontalLayout_5.addWidget(self.label_password, 0, QtCore.Qt.AlignTop)
        self.field_password = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.field_password.sizePolicy().hasHeightForWidth())
        self.field_password.setSizePolicy(sizePolicy)
        self.field_password.setObjectName("field_password")
        self.horizontalLayout_5.addWidget(self.field_password, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(2, 100)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.widget, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_9)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_headers = QtWidgets.QLabel(self.tab_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_headers.sizePolicy().hasHeightForWidth())
        self.label_headers.setSizePolicy(sizePolicy)
        self.label_headers.setStyleSheet("font: 18pt;")
        self.label_headers.setObjectName("label_headers")
        self.verticalLayout_3.addWidget(self.label_headers, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_name = QtWidgets.QLabel(self.tab_9)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout_7.addWidget(self.label_name, 0, QtCore.Qt.AlignTop)
        self.field_name = QtWidgets.QLineEdit(self.tab_9)
        self.field_name.setObjectName("field_name")
        self.horizontalLayout_7.addWidget(self.field_name, 0, QtCore.Qt.AlignTop)
        self.label_value = QtWidgets.QLabel(self.tab_9)
        self.label_value.setObjectName("label_value")
        self.horizontalLayout_7.addWidget(self.label_value, 0, QtCore.Qt.AlignTop)
        self.field_value = QtWidgets.QLineEdit(self.tab_9)
        self.field_value.setObjectName("field_value")
        self.horizontalLayout_7.addWidget(self.field_value, 0, QtCore.Qt.AlignTop)
        self.button_add = QtWidgets.QPushButton(self.tab_9)
        self.button_add.setObjectName("button_add")
        self.horizontalLayout_7.addWidget(self.button_add, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.table_headers = QtWidgets.QTableWidget(self.tab_9)
        self.table_headers.setObjectName("table_headers")
        self.table_headers.setColumnCount(2)
        self.table_headers.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_headers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_headers.setHorizontalHeaderItem(1, item)
        self.table_headers.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.table_headers)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.clear_button = QtWidgets.QPushButton(self.tab_9)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout_10.addWidget(self.clear_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.delete_header_button = QtWidgets.QPushButton(self.tab_9)
        self.delete_header_button.setObjectName("delete_header_button")
        self.horizontalLayout_10.addWidget(self.delete_header_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.tab_8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_2 = QtWidgets.QLabel(self.tab_8)
        self.label_2.setStyleSheet("font: 18pt;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_12.addWidget(self.label_2)
        self.status_code_label = QtWidgets.QLabel(self.tab_8)
        self.status_code_label.setObjectName("status_code_label")
        self.horizontalLayout_12.addWidget(self.status_code_label)
        self.field_status_code = QtWidgets.QLineEdit(self.tab_8)
        self.field_status_code.setReadOnly(True)
        self.field_status_code.setObjectName("field_status_code")
        self.horizontalLayout_12.addWidget(self.field_status_code)
        self.horizontalLayout_12.setStretch(0, 100)
        self.horizontalLayout_12.setStretch(2, 5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
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
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSupport = QtWidgets.QAction(MainWindow)
        self.actionSupport.setObjectName("actionSupport")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_2.setObjectName("actionOpen_2")
        self.menuProgram.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionSupport)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())
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
        self.label_3.setText(_translate("MainWindow", "Authentication "))
        self.label.setText(_translate("MainWindow", "Type"))
        self.auth_typ_cbox.setItemText(0, _translate("MainWindow", "Basic"))
        self.auth_typ_cbox.setItemText(1, _translate("MainWindow", "Digest"))
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
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.delete_header_button.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Headers"))
        self.label_2.setText(_translate("MainWindow", "Response"))
        self.status_code_label.setText(_translate("MainWindow", "Status code"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "Response"))
        self.menuProgram.setTitle(_translate("MainWindow", "Program"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionSupport.setText(_translate("MainWindow", "Support"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen_2.setText(_translate("MainWindow", "Open"))
