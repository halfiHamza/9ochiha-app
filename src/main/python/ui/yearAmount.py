# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Design\yearAmount.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_YearForm(object):
    def setupUi(self, YearForm):
        YearForm.setObjectName("YearForm")
        YearForm.resize(402, 212)
        self.verticalLayout = QtWidgets.QVBoxLayout(YearForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(YearForm)
        self.label.setStyleSheet("font: 25pt \"Audiowide\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.totalLabel = QtWidgets.QLabel(YearForm)
        self.totalLabel.setStyleSheet("font: 25pt \"Audiowide\";")
        self.totalLabel.setText("")
        self.totalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalLabel.setObjectName("totalLabel")
        self.verticalLayout.addWidget(self.totalLabel)

        self.retranslateUi(YearForm)
        QtCore.QMetaObject.connectSlotsByName(YearForm)

    def retranslateUi(self, YearForm):
        _translate = QtCore.QCoreApplication.translate
        YearForm.setWindowTitle(_translate("YearForm", "Kochiha App"))
        self.label.setText(_translate("YearForm", "Yearly Amount"))
