import sqlite3
from sqlite3 import Error
import pandas as pd
from itertools import *
from datetime import datetime


class DbConnecter(object):
    def __init__(self, db_file) -> None:
        super(DbConnecter, self).__init__()
        self.conn = None
        self.db_file = db_file
        self.tables = '''
        CREATE TABLE IF NOT EXISTS tasks (
            id integer PRIMARY KEY,
            day date,
            receive_n integer,
            item text VARCHAR(255),
            price real,
            remark text VARCHAR(255)
        );
        '''
        try:
            self.conn = sqlite3.connect(db_file)
            self.curser = self.conn.cursor()
            self.curser.execute(self.tables)
        except Error as e:
            print(e)
        # finally:
        #     if self.conn:
        #         self.conn.close()

    def InsertData(self, data):
        try:
            self.curser.execute(
                f"INSERT INTO tasks(day,receive_n,item,price,remark) VALUES(?,?,?,?,?)", data
            )
            self.conn.commit()
            return True
        except Error as e:
            return e

    def DailyAmount(self):
        result = self.curser.execute(
            f"SELECT day, SUM(price) FROM tasks GROUP BY day"
        )
        return sorted(result.fetchall(), key=lambda x: datetime.strptime(x[0], '%d/%m/%Y'))

    def MonthlyAmount(self):
        final = {}
        result = self.curser.execute(
            f"SELECT day, SUM(price) FROM tasks "
        )
        for i in result.fetchall():
            key = i[0][3:]
            if key in final:
                final[key] = final.get(key) + i[1]
            else:
                final[key] = i[1]

        return final

    def YearlyAmount(self):
        result = self.curser.execute(
            "SELECT SUM(price) FROM tasks"
        )

        return result.fetchall()[0][0]
