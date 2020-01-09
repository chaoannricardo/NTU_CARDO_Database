# -*- coding: utf8 -*-
from numpy import int64 as np_int64
from numpy import float64 as np_float64
from pymysql import connect as pymysql_connect
from sys import exit as sys_exit
from pymysql import cursors


class DatabaseConnection:
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
        try:
            # Test whether the type is pandas dataframe
            self.data.iloc[0:0] = self.data.iloc[0:0]
        except:
            print("# System error occurred within DatabaseManagement.py (data type incorrect.)")

    def commit(self):
        # Connect to MySQL Server
        while True:
            try:
                print('# 連接至MySQL資料庫....')
                conn = pymysql_connect(**self.config)
                cursor_object = conn.cursor()
                # Execute SQL command
                print(self.command)
                cursor_object.execute(self.command)
                # Reset command content
                self.command = ""
            except BaseException:
                print("# 連接失敗，程式終止")
                sys_exit(0)
                break
            else:
                print("# 連接成功，資料庫指令成功執行")
                break

    # Create table for activity
    def create(self):
        column_sql_dict = {
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
        self.command = "CREATE TABLE " + str(self.table_name) + " ("
        try:
            for i, j in enumerate(self.data.columns):
                if (i + 1) != len(self.data.columns):
                    if j in column_sql_dict:
                        self.command = self.command + j + " " + column_sql_dict[j] + ", "
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
                    if j in column_sql_dict:
                        self.command = self.command + j + " " + column_sql_dict[j] + ")"
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
    def insert_csv(self):
        for a in range(len(self.data)):
            column_command = []
            values_command = []
            for i, j in enumerate(self.data.columns):
                column_command.append(self.data.columns[i])
                values_command.append(self.data.iloc[a, i])
            # create the command
            command = "INSERT INTO " + self.table_name + " ("
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


if __name__ == '__main__':
    config = Main.log_in()
    conn = pymysql_connect(**config)
    cursor_object = conn.cursor()
    # Execute SQL command
    command = "INSERT INTO 20191026_TIP_企業實習計劃說明會_藍天百腦匯 (報名時間, 姓名, 身分證字號, 性別, 生日, 身份別, 一級單位, 二級單位, 職稱, 聯絡電話, 電子郵件, 餐食, 是否需要公務員時數, 成績, 合格否, 出席否, 合格證號, 備註, 網路位址, 帳號, 學位學分, 課程類別代碼, 學習類別, 上課縣市, 期別, 訓練總時數, 訓練總數單位, 數位時數, 實體時數, 是否有實習過？, 年度, 學期, 年度學期, 類別, 場次, 報名方式, CARDO點數, 是否計算黑名單) VALUES ('03  6 2019  5:49PM            ', '王?明', 'A130959713', '女', '01/10/1999                    ', '學生', '管理學院                      ', '財金系', '學士班', '988654950', 'nan', '其它', '是', '                              ', 'nan', '是', 'nan', 'nan', 'nan', 'b06703072', 6, '    ', 'p', '10', '2', 107, '1', 1, 10, 'nan', 106, 1, '106-1', 'TCP_希望種子培育計畫', '藍天', '現場報名', 0, '0');"
    cursor_object.execute(command)
    conn.commit()