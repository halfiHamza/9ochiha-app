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
                self.tableWidget.setItem(i, 0, QTableWidgetItem(str(k)))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(data[k])))
                self.tableWidget.setItem(
                    i, 2, QTableWidgetItem(str(data[k] - charge)))
        self.show()


class DailyAmount(QWidget, Ui_DailyForm):
    def __init__(self):
        super(DailyAmount, self).__init__()
        self.setupUi(self)

    def setData(self, data):
        if data:
            self.tableWidget.setRowCount(len(data))
            for i, a in enumerate(data):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(a[0]))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(a[1])))
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
        self.header = ['id', 'day', 'receive_n', 'item', 'price', 'remark']
        self.dateEdit.setDate(QDate.currentDate())
        self.socket = DbConnecter(db_file=db_file)
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.db_file)
        self.insert_tbtn.clicked.connect(self.insert)
        self.refresh_tbtn.clicked.connect(lambda: self.loadDb('All'))
        self.search.textChanged.connect(self.loadDb)
        # calcul amount
        self.Daily_tbtn.clicked.connect(
            lambda: self.day.setData(self.socket.DailyAmount()))
        self.Monthly_tbtn.clicked.connect(
            lambda: self.month.setData(self.socket.MonthlyAmount(), self.monthlyCharges.value()))
        self.Yearly_tbtn.clicked.connect(
            lambda: self.year.setTotal(str(self.socket.YearlyAmount())))
        self.loadDb('All')

    def insert(self):
        self.socket.InsertData(
            (self.dateEdit.date().toPyDate().strftime("%d/%m/%Y"),
             self.receiveNspinBox.value(),
             self.ItemLineEdit.text(),
             self.PriceDoubleSpinBox.value(),
             self.RemarkPlainTextEdit.toPlainText()
             )
        )
        self.loadDb('All')
        self.toolButton_2.click()

    def search(self, text):
        self.db.open()
        index = 0
        query = QSqlQuery()
        query.exec_("select * from tasks")
        if text == 'All':
            data = self.db.execute_query("SELECT id, c_type, c_name, concat(current_balance, ' {0}') FROM com_clients".format(
                self.currencySymbolLineEdit.text()))
        else:
            data = self.db.execute_query(
                "SELECT id, c_type, c_name, concat(current_balance, ' {1}') FROM com_clients "
                "WHERE id LIKE '{0}%' OR date LIKE '{0}%' OR c_type LIKE '{0}%' OR c_name LIKE '{0}%' OR c_address LIKE '{0}%' OR tlf_fax LIKE '{0}%' OR "
                "mob LIKE '{0}%' OR email LIKE '{0}%' OR register_n LIKE '{0}%' OR tin LIKE '{0}%' OR ti LIKE '{0}%' OR si LIKE '{0}%' OR technician LIKE '{0}%'".format(
                    text, self.currencySymbolLineEdit.text())
            )

    def loadDb(self, text):
        self.db.open()
        index = 0
        query = QSqlQuery()
        if text == 'All':
            query.exec_("select * from tasks ORDER BY day ASC")
        else:
            query.exec_(
                f"select * from tasks where receive_n like '{text}%' or item like '{text}%' or price like '{text}%' ORDER BY day ASC"
            )
        while query.next():
            ids = query.value(0)
            day = query.value(1)
            Receive_numbers = query.value(2)
            items = query.value(3)
            prices = query.value(4)
            remarks = query.value(5)
            self.tableWidget.setRowCount(index + 1)
            self.tableWidget.setItem(index, 0, QTableWidgetItem(str(ids)))
            self.tableWidget.setItem(index, 1, QTableWidgetItem(str(day)))
            self.tableWidget.setItem(
                index, 2, QTableWidgetItem(str(Receive_numbers)))
            self.tableWidget.setItem(index, 3, QTableWidgetItem(items))
            self.tableWidget.setItem(index, 4, QTableWidgetItem(str(prices)))
            self.tableWidget.setItem(index, 5, QTableWidgetItem(remarks))
            index += 1

        self.db.close()
        for i in range(index):
            # Add edit and delete buttons in the last cell
            self.tableWidget.setCellWidget(
                i, 6, self.buttonForRow())

    def UpdateButton(self):
        global liste
        liste = []
        current_row = self.tableWidget.currentRow()
        current_column = self.tableWidget.currentColumn()
        cell_value = self.tableWidget.item(current_row, current_column).text()
        button = self.sender()
        if button:
            for i in range(6):
                liste.append(self.tableWidget.item(
                    self.tableWidget.currentRow(), i).text())
            if current_column == 0:
                self.msg = QMessageBox(QMessageBox.Information, "Kochiha App",
                                       "Rak baghi tnik sog yalbobo", QMessageBox.Ok)
                self.msg.show()
            else:
                self.socket.curser.execute(f'''
                UPDATE tasks SET {self.header[current_column]} = "{cell_value}" WHERE id = {liste[0]};
                ''')
                self.socket.conn.commit()
            self.loadDb('All')

    def DeleteButton(self, event):
        global liste
        liste = []
        button = self.sender()
        if button:
            for i in range(6):
                liste.append(self.tableWidget.item(
                    self.tableWidget.currentRow(), i).text())
            replay = QMessageBox.information(
                self, "Kochiha App", "Really nigga", QMessageBox.Yes | QMessageBox.No)
            if replay == QMessageBox.Yes:
                self.socket.curser.execute(f'''
                DELETE FROM tasks WHERE id = {liste[0]};
                ''')
                self.socket.conn.commit()
                # This is the key when determining the location
                row = self.tableWidget.indexAt(button.parent().pos()).row()
                self.tableWidget.removeRow(row)
                self.loadDb('All')

    def buttonForRow(self):
        widget = QWidget()
        # Modify
        self.updateBtn = QPushButton('modify')
        self.updateBtn.setStyleSheet(''' text-align : center;
                                          background-color : NavajoWhite;
                                          height : 30px;
                                          border-style: outset;
                                          font : 13px  ''')

        # Delete
        self.deleteBtn = QPushButton('delete')
        self.deleteBtn.setStyleSheet(''' text-align : center;
                                    background-color : LightCoral;
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
