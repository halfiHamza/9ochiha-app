# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Design\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1198, 578)
        MainWindow.setStyleSheet("*{\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 12pt;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(400, 0))
        self.frame.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.toolButton_2 = QtWidgets.QToolButton(self.frame)
        self.toolButton_2.setMinimumSize(QtCore.QSize(132, 35))
        self.toolButton_2.setStyleSheet("background-color: #3498db;\n"
"border-radius: 4px;\n"
"border: none;")
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout_2.addWidget(self.toolButton_2, 5, 1, 1, 1)
        self.insert_tbtn = QtWidgets.QToolButton(self.frame)
        self.insert_tbtn.setMinimumSize(QtCore.QSize(120, 35))
        self.insert_tbtn.setStyleSheet("background-color: #2ecc71;\n"
"border: none;\n"
"border-radius: 4px;")
        self.insert_tbtn.setObjectName("insert_tbtn")
        self.gridLayout_2.addWidget(self.insert_tbtn, 5, 2, 1, 1)
        self.RemarkPlainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.RemarkPlainTextEdit.setObjectName("RemarkPlainTextEdit")
        self.gridLayout_2.addWidget(self.RemarkPlainTextEdit, 4, 1, 1, 2)
        self.PriceDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.PriceDoubleSpinBox.setMinimumSize(QtCore.QSize(0, 35))
        self.PriceDoubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.PriceDoubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.PriceDoubleSpinBox.setMaximum(1e+47)
        self.PriceDoubleSpinBox.setObjectName("PriceDoubleSpinBox")
        self.gridLayout_2.addWidget(self.PriceDoubleSpinBox, 3, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(0, 35))
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setMinimumSize(QtCore.QSize(0, 35))
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMinimumSize(QtCore.QSize(0, 35))
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setMinimumSize(QtCore.QSize(0, 35))
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 6, 1, 1, 1)
        self.ItemLineEdit = QtWidgets.QLineEdit(self.frame)
        self.ItemLineEdit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.ItemLineEdit.setFont(font)
        self.ItemLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ItemLineEdit.setObjectName("ItemLineEdit")
        self.gridLayout_2.addWidget(self.ItemLineEdit, 2, 1, 1, 2)
        self.receiveNspinBox = QtWidgets.QSpinBox(self.frame)
        self.receiveNspinBox.setMinimumSize(QtCore.QSize(0, 35))
        self.receiveNspinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.receiveNspinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.receiveNspinBox.setMaximum(999999999)
        self.receiveNspinBox.setObjectName("receiveNspinBox")
        self.gridLayout_2.addWidget(self.receiveNspinBox, 1, 1, 1, 2)
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 0, 1, 1, 2)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(40)
        self.gridLayout_3.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.refresh_tbtn = QtWidgets.QToolButton(self.frame_2)
        self.refresh_tbtn.setMinimumSize(QtCore.QSize(0, 35))
        self.refresh_tbtn.setObjectName("refresh_tbtn")
        self.horizontalLayout_4.addWidget(self.refresh_tbtn)
        self.search = QtWidgets.QLineEdit(self.frame_2)
        self.search.setMinimumSize(QtCore.QSize(300, 35))
        self.search.setMaximumSize(QtCore.QSize(300, 16777215))
        self.search.setAlignment(QtCore.Qt.AlignCenter)
        self.search.setObjectName("search")
        self.horizontalLayout_4.addWidget(self.search)
        self.Daily_tbtn = QtWidgets.QToolButton(self.frame_2)
        self.Daily_tbtn.setMinimumSize(QtCore.QSize(0, 35))
        self.Daily_tbtn.setObjectName("Daily_tbtn")
        self.horizontalLayout_4.addWidget(self.Daily_tbtn)
        self.Monthly_tbtn = QtWidgets.QToolButton(self.frame_2)
        self.Monthly_tbtn.setMinimumSize(QtCore.QSize(0, 35))
        self.Monthly_tbtn.setObjectName("Monthly_tbtn")
        self.horizontalLayout_4.addWidget(self.Monthly_tbtn)
        self.Yearly_tbtn = QtWidgets.QToolButton(self.frame_2)
        self.Yearly_tbtn.setMinimumSize(QtCore.QSize(0, 35))
        self.Yearly_tbtn.setObjectName("Yearly_tbtn")
        self.horizontalLayout_4.addWidget(self.Yearly_tbtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(80, 80))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/img/src/main/resources/img/Icon.ico"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Audiowide")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 25pt \"Audiowide\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setMaximumSize(QtCore.QSize(125, 16777215))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.monthlyCharges = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.monthlyCharges.setMinimumSize(QtCore.QSize(0, 35))
        self.monthlyCharges.setMaximumSize(QtCore.QSize(200, 16777215))
        self.monthlyCharges.setAlignment(QtCore.Qt.AlignCenter)
        self.monthlyCharges.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.monthlyCharges.setMaximum(1e+43)
        self.monthlyCharges.setProperty("value", 492000.0)
        self.monthlyCharges.setObjectName("monthlyCharges")
        self.horizontalLayout.addWidget(self.monthlyCharges)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolButton_2.clicked.connect(self.RemarkPlainTextEdit.clear)
        self.toolButton_2.clicked.connect(self.ItemLineEdit.clear)
        self.toolButton_2.clicked.connect(self.receiveNspinBox.clear)
        self.toolButton_2.clicked.connect(self.PriceDoubleSpinBox.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.dateEdit, self.receiveNspinBox)
        MainWindow.setTabOrder(self.receiveNspinBox, self.ItemLineEdit)
        MainWindow.setTabOrder(self.ItemLineEdit, self.PriceDoubleSpinBox)
        MainWindow.setTabOrder(self.PriceDoubleSpinBox, self.RemarkPlainTextEdit)
        MainWindow.setTabOrder(self.RemarkPlainTextEdit, self.insert_tbtn)
        MainWindow.setTabOrder(self.insert_tbtn, self.toolButton_2)
        MainWindow.setTabOrder(self.toolButton_2, self.search)
        MainWindow.setTabOrder(self.search, self.refresh_tbtn)
        MainWindow.setTabOrder(self.refresh_tbtn, self.Daily_tbtn)
        MainWindow.setTabOrder(self.Daily_tbtn, self.Monthly_tbtn)
        MainWindow.setTabOrder(self.Monthly_tbtn, self.Yearly_tbtn)
        MainWindow.setTabOrder(self.Yearly_tbtn, self.tableWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kochiha App"))
        self.toolButton_2.setText(_translate("MainWindow", "Clear"))
        self.insert_tbtn.setText(_translate("MainWindow", "Add"))
        self.label_3.setText(_translate("MainWindow", "Date:"))
        self.label_5.setText(_translate("MainWindow", "Item:"))
        self.label_4.setText(_translate("MainWindow", "Receive number:"))
        self.label_6.setText(_translate("MainWindow", "Price:"))
        self.label_7.setText(_translate("MainWindow", "Remark:"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Receive N°"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Item"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Remark"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Operating"))
        self.refresh_tbtn.setText(_translate("MainWindow", "Refresh"))
        self.search.setPlaceholderText(_translate("MainWindow", "Search"))
        self.Daily_tbtn.setText(_translate("MainWindow", "Daily amount"))
        self.Monthly_tbtn.setText(_translate("MainWindow", "Monthly amount"))
        self.Yearly_tbtn.setText(_translate("MainWindow", "Yearly amount"))
        self.label.setText(_translate("MainWindow", "Sarl PC-FIX"))
        self.label_8.setText(_translate("MainWindow", "Monthly charges"))
import assets_rc
