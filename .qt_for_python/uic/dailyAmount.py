# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ghost\Desktop\9ochiha app\Design\dailyAmount.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DailyForm(object):
    def setupUi(self, DailyForm):
        DailyForm.setObjectName("DailyForm")
        DailyForm.resize(500, 576)
        DailyForm.setMaximumSize(QtCore.QSize(500, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(DailyForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(DailyForm)
        self.label.setStyleSheet("font: 25pt \"Audiowide\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(DailyForm)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setMinimumSectionSize(40)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(DailyForm)
        QtCore.QMetaObject.connectSlotsByName(DailyForm)

    def retranslateUi(self, DailyForm):
        _translate = QtCore.QCoreApplication.translate
        DailyForm.setWindowTitle(_translate("DailyForm", "Kochiha App"))
        self.label.setText(_translate("DailyForm", "Daily Amount"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DailyForm", "Day date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DailyForm", "Day amount"))
