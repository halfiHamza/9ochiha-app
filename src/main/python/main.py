import imp
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from ui.mainWindow import Ui_MainWindow
from ui.yearAmount import Ui_YearForm
from ui.monthAmount import Ui_MonthForm
from ui.dayAmount import Ui_DailyForm
import sys
from db import DbConnecter
from datetime import datetime


class YearlyAmount(QWidget, Ui_YearForm):
    def __init__(self):
        super(YearlyAmount, self).__init__()
        self.setupUi(self)

    def setTotal(self, total):
        self.totalLabel.setText(total + " DZA")
        self.show()


class MonthlyAmount(QWidget, Ui_MonthForm):
    def __init__(self):
        super(MonthlyAmount, self).__init__()
        self.setupUi(self)

    def setData(self, data=None, charge=None):
        if data:
            self.tableWidget.setRowCount(len(data))
            for i, k in enumerate(data):
                date = QTableWidgetItem(str(k))
                date.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i, 0, date)
                amount = QTableWidgetItem(str(data[k]) + ' DA')
                amount.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i, 1, amount)
                subCharge = QTableWidgetItem(str(data[k] - charge) + ' DA')
                subCharge.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i, 2, subCharge)
        self.show()


class DailyAmount(QWidget, Ui_DailyForm):
    def __init__(self):
        super(DailyAmount, self).__init__()
        self.setupUi(self)

    def setData(self, data):
        if data:
            self.tableWidget.setRowCount(len(data))
            for i, a in enumerate(data):
                day = QTableWidgetItem(a[0])
                day.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i, 0, day)
                amount = QTableWidgetItem(str(a[1]) + ' DA')
                amount.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i, 1, amount)
        self.show()


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, db_file):
        super(App, self).__init__()
        self.setupUi(self)
        self.db_file = db_file
        # ui init
        self.year = YearlyAmount()
        self.month = MonthlyAmount()
        self.day = DailyAmount()
        self.header = ['Day', 'Receive_n', 'Item', 'Price', 'Remark']
        self.dateEdit.setDate(QDate.currentDate())
        self.db = DbConnecter(self.db_file)
        self.insert_tbtn.clicked.connect(self.insert)
        self.refresh_tbtn.clicked.connect(lambda: self.loadDb('All'))
        self.search.textChanged.connect(self.loadDb)
        # calcul amount
        self.Daily_tbtn.clicked.connect(
            lambda: self.day.setData(self.db.DailyAmount()))
        self.Monthly_tbtn.clicked.connect(
            lambda: self.month.setData(self.db.MonthlyAmount(), self.monthlyCharges.value()))
        self.Yearly_tbtn.clicked.connect(
            lambda: self.year.setTotal(str(self.db.YearlyAmount())))
        self.loadDb('All')

    def insert(self):
        self.db.InsertData(
            (self.dateEdit.date().toPyDate().strftime("%d/%m/%Y"),
             self.receiveNspinBox.value(),
             self.ItemLineEdit.text(),
             self.PriceDoubleSpinBox.value(),
             self.RemarkPlainTextEdit.toPlainText()
             )
        )
        self.loadDb('All')
        self.toolButton_2.click()

    def loadDb(self, text):
        '''
            day date,
            receive_n integer,
            item text VARCHAR(255),
            price real,
            remark text VARCHAR(255)
        '''
        index = 0
        if text == 'All':
            result = self.db.curser.execute(
                "select day, receive_n, item, price, remark from tasks")
        else:
            result = self.db.curser.execute(
                f"select day, receive_n, item, price, remark from tasks where receive_n like '{text}%' or item like '{text}%' or price like '{text}%'"
            )
        data = sorted(result.fetchall(),
                      key=lambda x: datetime.strptime(x[0], '%d/%m/%Y'))
        finalData = reversed(data)
        for i in finalData:
            day = QTableWidgetItem(str(i[0]))
            day.setTextAlignment(Qt.AlignCenter)
            Receive_numbers = QTableWidgetItem(str(i[1]))
            Receive_numbers.setTextAlignment(Qt.AlignCenter)
            items = QTableWidgetItem(str(i[2]))
            items.setTextAlignment(Qt.AlignCenter)
            prices = QTableWidgetItem(str(i[3]) + ' DA')
            prices.setTextAlignment(Qt.AlignCenter)
            remarks = QTableWidgetItem(str(i[4]))
            remarks.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setRowCount(index + 1)
            self.tableWidget.setItem(index, 0, day)
            self.tableWidget.setItem(
                index, 1, Receive_numbers)
            self.tableWidget.setItem(index, 2, items)
            self.tableWidget.setItem(index, 3, prices)
            self.tableWidget.setItem(index, 4, remarks)
            index += 1

        for i in range(index):
            self.tableWidget.setCellWidget(
                i, 5, self.buttonForRow())

    def UpdateButton(self):
        global liste
        liste = []
        current_row = self.tableWidget.currentRow()
        if current_row != -1:
            current_column = self.tableWidget.currentColumn()
            cell_value = self.tableWidget.item(
                current_row, current_column).text()
            button = self.sender()
            if button:
                for i in range(5):
                    liste.append(self.tableWidget.item(
                        self.tableWidget.currentRow(), i).text())
                self.db.curser.execute(
                    f"UPDATE tasks SET {self.header[current_column]} = '{cell_value}' WHERE day = '{liste[0]}' AND receive_n = '{liste[1]}' AND item = '{liste[2]}' AND price = '{liste[3]}' AND remark = '{liste[4]}'")
                self.loadDb('All')

    def DeleteButton(self, event):
        global liste
        liste = []
        button = self.sender()
        if button:
            for i in range(5):
                liste.append(self.tableWidget.item(
                    self.tableWidget.currentRow(), i).text())
            replay = QMessageBox.information(
                self, "Kochiha App", "Really nigga", QMessageBox.Yes | QMessageBox.No)
            if replay == QMessageBox.Yes:
                self.db.curser.execute(
                    f"DELETE FROM tasks WHERE day = '{liste[0]}' AND receive_n = '{liste[1]}' AND item = '{liste[2]}' AND price = '{liste[3]}' AND remark = '{liste[4]}'")
                # This is the key when determining the location
                row = self.tableWidget.indexAt(button.parent().pos()).row()
                self.tableWidget.removeRow(row)
                self.loadDb('All')

    def buttonForRow(self):
        widget = QWidget()
        # Modify
        self.updateBtn = QPushButton('Edit')
        self.updateBtn.setStyleSheet(''' text-align : center;
                                          background-color : #2ecc71;
                                          height : 30px;
                                          border-style: outset;
                                          font : 13px  ''')

        # Delete
        self.deleteBtn = QPushButton('Delete')
        self.deleteBtn.setStyleSheet(''' text-align : center;
                                    background-color : #e74c3c;
                                    height : 30px;
                                    border-style: outset;
                                    font : 13px; ''')
        self.deleteBtn.clicked.connect(self.DeleteButton)
        self.updateBtn.clicked.connect(self.UpdateButton)

        hLayout = QHBoxLayout()
        hLayout.addWidget(self.updateBtn)
        hLayout.addWidget(self.deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    QFontDatabase.addApplicationFont(
        appctxt.get_resource('fonts/Audiowide-Regular.ttf'))
    window = App(db_file=appctxt.get_resource(
        'database/kochiha.db').replace("\\", "/"))
    window.showMaximized()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
