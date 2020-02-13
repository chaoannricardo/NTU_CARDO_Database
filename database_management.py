# -*- coding: utf8 -*-
from numpy import int64 as np_int64
from numpy import float64 as np_float64
from pandas import read_sql as pd_read_sql
from pymysql import connect as pymysql_connect
from pymysql import cursors
from sys import exit as sys_exit
from time import localtime
import __init__


class DataConnection:
    def __init__(self, data, config, first_cat, second_cat, date):
        self.config = config
        self.data = data
        self.table_name = date + "_" + first_cat + "_" + second_cat
        self.first_cat = first_cat
        self.second_cat = second_cat
        self.date = date
        self.year = date[0:4]
        self.month = date[4:6]
        self.day = data[6:]
        self.command = ""
        self.column_sql_dict = {
            "報名時間": "VARCHAR(100)",
            "姓名": "VARCHAR(100)",
            "身分證字號": "VARCHAR(100)",
            "性別": "VARCHAR(100)",
            "生日": "VARCHAR(100)",
            "身份別": "VARCHAR(100)",
            "一級單位": "VARCHAR(100)",
            "二級單位": "VARCHAR(100)",
            "職稱": "VARCHAR(100)",
            "聯絡電話": "VARCHAR(100)",
            "電子郵件": "VARCHAR(100)",
            "餐食": "VARCHAR(100)",
            "是否需要公務員時數": "VARCHAR(100)",
            "成績": "VARCHAR(100)",
            "合格否": "VARCHAR(100)",
            "出席否": "VARCHAR(100)",
            "合格證號": "VARCHAR(100)",
            "備註": "VARCHAR(100)",
            "網路位址": "VARCHAR(100)",
            "帳號": "VARCHAR(100)",
            "學位學分": "INT",
            "課程類別代碼": "VARCHAR(100)",
            "學習類別": "VARCHAR(100)",
            "上課縣市": "VARCHAR(100)",
            "期別": "VARCHAR(100)",
            "訓練總時數": "INT",
            "訓練總數單位": "VARCHAR(100)",
            "數位時數": "INT",
            "實體時數": "INT",
            "是否有實習過？": "VARCHAR(100)",
            "年度": "INT",
            "學期": "INT",
            "年度學期": "VARCHAR(100)",
            "類別": "VARCHAR(100)",
            "場次": "VARCHAR(100)",
            "報名方式": "VARCHAR(100)",
            "CARDO點數": "INT",
            "是否計算黑名單": "VARCHAR(100)"
        }
        try:
            # Test whether the type is pandas dataframe
            self.data.iloc[0:0] = self.data.iloc[0:0]
        except:
            print("# System error occurred within DatabaseManagement.py (data type incorrect.)")

    # Produce create command
    def create_table(self, table_name):
        self.command = "CREATE TABLE " + str(table_name) + " ("
        try:
            for i, j in enumerate(self.data.columns):
                if (i + 1) != len(self.data.columns):
                    if j in self.column_sql_dict:
                        self.command = self.command + j + " " + self.column_sql_dict[j] + ", "
                    else:
                        if type(self.data.iloc[0, i]) == str:
                            self.command = self.command + j + " VARCHAR(100), "
                        elif type(self.data.iloc[0, i]) == np_int64:
                            self.command = self.command + j + " INT, "
                        elif type(self.data.iloc[0, i]) == np_float64:
                            self.command = self.command + j + " INT, "
                        else:
                            print("Type not found.")
                else:
                    if j in self.column_sql_dict:
                        self.command = self.command + j + " " + self.column_sql_dict[j] + ")"
                    else:
                        if type(self.data.iloc[0, i]) == str:
                            self.command = self.command + j + " VARCHAR(100))"
                        elif type(self.data.iloc[0, i]) == np_int64:
                            self.command = self.command + j + " INT)"
                        elif type(self.data.iloc[0, i]) == np_float64:
                            self.command = self.command + j + " INT)"
                        else:
                            print("Type not found.")
        except:
            for i, j in enumerate(self.data.columns):
                if (i + 1) != len(self.data.columns):
                    if type(self.data.iloc[0, i]) == str:
                        self.command = self.command + j + " VARCHAR(100),"
                    elif type(self.data.iloc[0, i]) == np_int64:
                        self.command = self.command + j + " INT,"
                    elif type(self.data.iloc[0, i]) == np_float64:
                        self.command = self.command + j + " INT,"
                    else:
                        print("Type not found.")
                else:
                    if type(self.data.iloc[0, i]) == str:
                        self.command = self.command + j + " VARCHAR(100))"
                    elif type(self.data.iloc[0, i]) == np_int64:
                        self.command = self.command + j + " INT)"
                    elif type(self.data.iloc[0, i]) == np_float64:
                        self.command = self.command + j + " INT)"
                    else:
                        print("Type not found.")
        conn = pymysql_connect(**self.config)
        cursor_object = conn.cursor()
        # Execute SQL command
        cursor_object.execute(self.command)

    # Insert csv into separate table
    def insert_table(self, table_name):
        for a in range(len(self.data)):
            column_command = []
            values_command = []
            for i, j in enumerate(self.data.columns):
                column_command.append(self.data.columns[i])
                values_command.append(self.data.iloc[a, i])
            # create the command
            command = "INSERT INTO " + table_name + " ("
            for i, j in enumerate(column_command):
                if i != (len(column_command) - 1):
                    command += str(j) + ", "
                else:
                    command += str(j)
            command += ") VALUES ("
            for i, j in enumerate(column_command):
                int_list = ["學位學分", "訓練總時數", "數位時數", "實體時數", "年度", "學期", "CARDO點數"]
                if i != (len(column_command) - 1):
                    if j in int_list:
                        command += str(values_command[i]) + ", "
                    else:
                        command += "'" + str(values_command[i]) + "', "
                else:
                    if j in int_list:
                        command += str(values_command[i])
                    else:
                        command += "'" + str(values_command[i]) + "');"
            conn = pymysql_connect(**self.config)
            cursor_object = conn.cursor()
            # Execute SQL command
            cursor_object.execute(command)
            conn.commit()


class SimpleConnection:
    def __init__(self, config):
        self.config = config

    def black_list_search(self):
        print("# 是否只顯示進入黑名單（>=5）的同學列表？(Y/N)")
        yes_no = input("# 輸入N則會顯示所有同學目前的黑名單技術，並以降冪排序： ")
        yes_no_list = ["Y", "y", "N", "n"]
        while True:
            if yes_no not in yes_no_list:
                print("# 您所輸入的選項錯誤，請再輸入一次")
            elif yes_no == "Y" or yes_no == "y":
                self.command = "SELECT 姓名, SUM(是否計算黑名單) AS \"黑名單次數\", SUM(CARDO點數) AS \"CARDO點數總計\", 電子郵件, 聯絡電話, 性別, 身份別, 一級單位, 二級單位, 職稱, 生日 FROM 主資料表 GROUP BY 姓名, 性別, 身份別, 一級單位, 二級單位, 職稱, 電子郵件, 聯絡電話, 生日 HAVING SUM(是否計算黑名單) >= 5 ORDER BY 黑名單次數 DESC;"
                break
            else:
                self.command = "SELECT 姓名, SUM(是否計算黑名單) AS \"黑名單次數\", SUM(CARDO點數) AS \"CARDO點數總計\", 電子郵件, 聯絡電話, 性別, 身份別, 一級單位, 二級單位, 職稱, 生日 FROM 主資料表 GROUP BY 姓名, 性別, 身份別, 一級單位, 二級單位, 職稱, 電子郵件, 聯絡電話, 生日 ORDER BY 黑名單次數 DESC;"
                break
        conn = pymysql_connect(**self.config)
        #cursor_object = conn.cursor()
        # Execute SQL command
        #cursor_object.execute(self.command)
        # read sql by pandas
        data = pd_read_sql(self.command, conn)
        time_stamp = str(localtime().tm_year) + str(localtime().tm_mon) + str(localtime().tm_mday)
        self.file_path = input("# 請輸入你所想存儲資料的路徑： ")
        self.file_path = self.file_path.replace("\\", "/").replace("\"", "") + "/" + time_stamp +"_blacklist_search.csv"
        data.to_csv(self.file_path, encoding="Big5", sep=",", index=False)


if __name__ == '__main__':
    print()
