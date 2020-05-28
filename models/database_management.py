# -*- coding: utf8 -*-
from numpy import int64 as np_int64
from numpy import float64 as np_float64
from pandas import read_sql as pd_read_sql
from pymysql import connect as pymysql_connect
from pymysql import cursors
from sys import exit as sys_exit
from time import localtime
from time import sleep as t_sleep
import pymysql
import configuration as conf


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
        self.column_sql_dict = conf.get_main_frame_dict()
        try:
            # Test whether the type is pandas dataframe
            self.data.iloc[0:0] = self.data.iloc[0:0]
        except:
            print("# System error occurred within DatabaseManagement.py (data type incorrect.)")

    # Produce create command
    def create_table(self, table_name, isMainTable=False):
        self.command = "CREATE TABLE " + str(table_name) + " ("
        try:
            maintable_column_list = list(conf.get_main_frame_dict().keys())
            for i, j in enumerate(self.data.columns):
                if (i + 1) != len(self.data.columns):
                    if j in self.column_sql_dict:
                        self.command = self.command + "`" + j + "` " + self.column_sql_dict[j] + ", "
                    else:
                        if type(self.data.iloc[0, i]) == str:
                            self.command = self.command + "`" + j + "` VARCHAR(100), "
                        elif type(self.data.iloc[0, i]) == np_int64:
                            self.command = self.command + "`" + j + "` INT, "
                        elif type(self.data.iloc[0, i]) == np_float64:
                            self.command = self.command + "`" + j + "` INT, "
                else:
                    if not isMainTable:
                        # last column of not creating main table
                        if j in self.column_sql_dict:
                            self.command = self.command + "`" + j + "` " + self.column_sql_dict[j] + ")"
                        else:
                            if type(self.data.iloc[0, i]) == str:
                                self.command = self.command + "`" + j + "` VARCHAR(100))"
                            elif type(self.data.iloc[0, i]) == np_int64:
                                self.command = self.command + "`" + j + "` INT)"
                            elif type(self.data.iloc[0, i]) == np_float64:
                                self.command = self.command + "`" + j + "` INT)"
                    else:
                        if all(item in self.data.columns for item in maintable_column_list):
                            if j in self.column_sql_dict:
                                self.command = self.command + "`" + j + "` " + self.column_sql_dict[j] + ")"
                            else:
                                if type(self.data.iloc[0, i]) == str:
                                    self.command = self.command + "`" + j + "` VARCHAR(100))"
                                elif type(self.data.iloc[0, i]) == np_int64:
                                    self.command = self.command + "`" + j + "` INT)"
                                elif type(self.data.iloc[0, i]) == np_float64:
                                    self.command = self.command + "`" + j + "` INT)"
                        # This part ensure that if you are creating main table,
                        # we would add all possible columns as our schema
                        else:
                            # append last column inside the data first
                            if j in self.column_sql_dict:
                                self.command = self.command + "`" + j + "` " + self.column_sql_dict[j] + ", "
                            else:
                                if type(self.data.iloc[0, i]) == str:
                                    self.command = self.command + "`" + j + "` VARCHAR(100), "
                                elif type(self.data.iloc[0, i]) == np_int64:
                                    self.command = self.command + "`" + j + "` INT, "
                                elif type(self.data.iloc[0, i]) == np_float64:
                                    self.command = self.command + "`" + j + "` INT, "
                            # then, append remain columns of main table
                            columns_needed_to_be_added = []
                            for a, b in enumerate(maintable_column_list):
                                if b not in self.data.columns:
                                    columns_needed_to_be_added.append(b)
                            for a, b in enumerate(columns_needed_to_be_added):
                                if (a + 1) != len(columns_needed_to_be_added):
                                    self.command = self.command + "`" + b + "` " + self.column_sql_dict[b] + ", "
                                else:
                                    self.command = self.command + "`" + b + "` " + self.column_sql_dict[b] + ")"
            # Execute SQL command
            conn = pymysql_connect(**self.config)
            cursor_object = conn.cursor()
            cursor_object.execute(self.command)
        except:
            for i, j in enumerate(self.data.columns):
                if (i + 1) != len(self.data.columns):
                    if j in self.column_sql_dict:
                        self.command = self.command + "`" + j + "` " + self.column_sql_dict[j] + ", "
                    else:
                        if type(self.data.iloc[0, i]) == str:
                            self.command = self.command + "`" + j + "` longtext, "
                        elif type(self.data.iloc[0, i]) == np_int64:
                            self.command = self.command + "`" + j + "` INT, "
                        elif type(self.data.iloc[0, i]) == np_float64:
                            self.command = self.command + "`" + j + "` INT, "
                else:
                    if j in self.column_sql_dict:
                        self.command = self.command + j + "` " + self.column_sql_dict[j] + ")"
                    else:
                        if type(self.data.iloc[0, i]) == str:
                            self.command = self.command + "`" + j + "` longtext"
                        elif type(self.data.iloc[0, i]) == np_int64:
                            self.command = self.command + "`" + j + "` INT)"
                        elif type(self.data.iloc[0, i]) == np_float64:
                            self.command = self.command + "`" + j + "` INT)"
            try:
                # Execute SQL command
                conn = pymysql_connect(**self.config)
                cursor_object = conn.cursor()
                cursor_object.execute(self.command)
            except pymysql.err.DataError:
                print("# 設計外錯誤發生，請聯絡程式管理員（database_management: create_table）")
                t_sleep(5)
                sys_exit()

    # Insert csv into separate table
    def insert_table(self, table_name):
        # create list of columns of mainframe
        conn = pymysql_connect(**self.config)
        show_column_command = "SHOW COLUMNS FROM " + table_name
        data = pd_read_sql(show_column_command, conn)
        maintable_column_list = data.iloc[:, 0].tolist()

        for a in range(len(self.data)):
            column_command = []
            values_command = []

            # initiate the columns that we would like to insert
            for i, j in enumerate(self.data.columns):
                column_command.append(self.data.columns[i])

            # check if all insert columns are inside main table
            if all(item in maintable_column_list for item in column_command):
                pass
            else:
                # drop the columns that is not inside main table
                for i, j in enumerate(column_command):
                    if j not in maintable_column_list:
                        print('# 欄位：', j, '不在被輸入表格內（通常是"主資料表"），因此將不會被輸入，\n' \
                                          '如果有需要輸入該值，請洽程式設計者')
                        column_command.remove(j)

            # revise and append value that we would like to insert
            for i, j in enumerate(column_command):
                values_command.append(self.data.loc[a, j])

            # create the command
            command = "INSERT INTO " + table_name + " ("
            for i, j in enumerate(column_command):
                if i != (len(column_command) - 1):
                    command += "`" + str(j) + "`, "
                else:
                    command += "`" + str(j) + "`"
            command += ") VALUES ("
            for i, j in enumerate(column_command):
                int_list = conf.get_db_number_list()
                if i != (len(column_command) - 1):
                    if j in int_list:
                        command += str(values_command[i]) + ", "
                    else:
                        command += "'" + str(values_command[i]) + "', "
                else:
                    if j in int_list:
                        command += str(values_command[i]) + "');"
                    else:
                        command += "'" + str(values_command[i]) + "');"

            conn = pymysql_connect(**self.config)
            cursor_object = conn.cursor()

            # Execute SQL command
            try:
                cursor_object.execute(command)
                conn.commit()
            except pymysql.err.DataError:
                t_sleep(5)
                print("# 設計外錯誤發生，請聯絡程式管理員（database_management: insert_table）")
                sys_exit()

    # Depreciated: since the alter command uses too much resources and may cause the db to crush
    def alter_table(self, table_name, column_command, maintable_column_list):
        print('# 新增新欄位於"主資料表"')
        # create list that is not inside mainframe
        columns_not_in_mainframe = []
        for i, j in enumerate(column_command):
            if j not in maintable_column_list:
                columns_not_in_mainframe.append(j)

        # alter maintable by adding columns not inside main table
        alter_command = "ALTER TABLE " + table_name + "\nADD COLUMN "
        try:
            for i, j in enumerate(columns_not_in_mainframe):
                if i != (len(columns_not_in_mainframe) - 1):
                    if type(self.data.loc[0, str(j)]) == str:
                        alter_command = alter_command + j + " VARCHAR(100), "
                    elif type(self.data.loc[0, str(j)]) == np_int64:
                        alter_command = alter_command + j + " INT, "
                    elif type(self.data.loc[0, str(j)]) == np_float64:
                        alter_command = alter_command + j + " INT, "
                else:
                    if type(self.data.loc[0, str(j)]) == str:
                        alter_command = alter_command + j + " VARCHAR(100)"
                    elif type(self.data.loc[0, str(j)]) == np_int64:
                        alter_command = alter_command + j + " INT"
                    elif type(self.data.loc[0, str(j)]) == np_float64:
                        alter_command = alter_command + j + " INT"

            # execute alter command
            conn = pymysql_connect(**self.config)
            cursor_object = conn.cursor()
            cursor_object.execute(alter_command)
            print("alter table finished")

        except pymysql.err.DataError:
            for i, j in enumerate(columns_not_in_mainframe):
                if i != (len(columns_not_in_mainframe) - 1):
                    if type(self.data.loc[0, str(j)]) == str:
                        alter_command = alter_command + j + " longtext, "
                    elif type(self.data.loc[0, str(j)]) == np_int64:
                        alter_command = alter_command + j + " INT, "
                    elif type(self.data.loc[0, str(j)]) == np_float64:
                        alter_command = alter_command + j + " INT, "
                else:
                    if type(self.data.loc[0, str(j)]) == str:
                        alter_command = alter_command + j + " longtext"
                    elif type(self.data.loc[0, str(j)]) == np_int64:
                        alter_command = alter_command + j + " INT"
                    elif type(self.data.loc[0, str(j)]) == np_float64:
                        alter_command = alter_command + j + " INT"

            # execute alter command
            conn = pymysql_connect(**self.config)
            cursor_object = conn.cursor()
            cursor_object.execute(alter_command)


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
                self.command = "SELECT 姓名, SUM(是否計算黑名單) AS \"黑名單次數\", SUM(CARDO點數) AS \"CARDO點數總計\", 電子郵件, 聯絡電話, 性別, " \
                               "身份別, 一級單位, 二級單位, 職稱, 生日 FROM 主資料表 GROUP BY 姓名, 性別, 身份別, 一級單位, 二級單位, 職稱, 電子郵件, 聯絡電話, " \
                               "生日 HAVING SUM(是否計算黑名單) >= 5 ORDER BY 黑名單次數 DESC; "
                break
            else:
                self.command = "SELECT 姓名, SUM(是否計算黑名單) AS \"黑名單次數\", SUM(CARDO點數) AS \"CARDO點數總計\", 電子郵件, 聯絡電話, 性別, " \
                               "身份別, 一級單位, 二級單位, 職稱, 生日 FROM 主資料表 GROUP BY 姓名, 性別, 身份別, 一級單位, 二級單位, 職稱, 電子郵件, 聯絡電話, " \
                               "生日 ORDER BY 黑名單次數 DESC; "
                break
        conn = pymysql_connect(**self.config)
        # cursor_object = conn.cursor()
        # Execute SQL command
        # cursor_object.execute(self.command)
        # read sql by pandas
        data = pd_read_sql(self.command, conn)
        time_stamp = str(localtime().tm_year) + str(localtime().tm_mon) + str(localtime().tm_mday)
        self.file_path = input("# 請輸入你所想存儲資料的路徑： ")
        self.file_path = self.file_path.replace("\\", "/").replace("\"",
                                                                   "") + "/" + time_stamp + "_blacklist_search.csv"
        data.to_csv(self.file_path, encoding="Big5", sep=",", index=False)


if __name__ == '__main__':
    # config = conf.auto_log_in()
    # command = "SHOW COLUMNS FROM cardo.主資料表"
    # conn = pymysql_connect(**config)
    # data = pd_read_sql(command, conn)
    # column_list = data.iloc[:, 0].tolist()
    # # print(data)
    # # print(data.shape)
    # print(column_list)
    a_list = [1, 2, 3]
    b_list = [1, 2, 3, 4, 5, 6]
    print(all(item in b_list for item in a_list))
