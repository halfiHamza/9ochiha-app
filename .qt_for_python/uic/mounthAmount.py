# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ghost\Desktop\9ochiha app\Design\mounthAmount.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MonthForm(object):
    def setupUi(self, MonthForm):
        MonthForm.setObjectName("MonthForm")
        MonthForm.resize(600, 383)
        MonthForm.setMaximumSize(QtCore.QSize(600, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(MonthForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(MonthForm)
        self.label.setStyleSheet("font: 25pt \"Audiowide\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(MonthForm)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(MonthForm)
        QtCore.QMetaObject.connectSlotsByName(MonthForm)

    def retranslateUi(self, MonthForm):
        _translate = QtCore.QCoreApplication.translate
        MonthForm.setWindowTitle(_translate("MonthForm", "Form"))
        self.label.setText(_translate("MonthForm", "Monthly Amount"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MonthForm", "Date per month"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MonthForm", "Monthly amount"))
