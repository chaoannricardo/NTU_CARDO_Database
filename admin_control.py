# -*- coding: utf8 -*-
from pandas import read_csv as pd_read_csv
from time import sleep as t_sleep
import configuration as conf
import database_management
import data_processing
import file_management
import pymysql
import __init__


def admin_control():
    print("【管理員模式】")
    print("0. 產生主表（本功能將需要一'已登錄出席'之出席統計表，）")
    command = input("# 請輸入您所需要的功能，或輸入'exit'返回主選單")
    if command == 'exit':
        print("# 返回主選單")
        t_sleep(1)
    elif command == "0":
        # "C:\Users\ricardo\Desktop\Data\0311_藍天百腦匯報名清單(登陸出席).csv"
        while True:
            account = input("# 請輸入帳號： ")
            password = input("# 請輸入密碼： ")
            try:
                config = conf.get_config(account, password)
                # 身分驗證
                print('# 登入中....')
                conn = database_management.pymysql_connect(**config)
                print("# 登入成功，歡迎回來", account, '\n\n')
                t_sleep(1)
                break
            except pymysql.err.OperationalError:
                print("# 您輸入的帳號或密碼錯誤，請再輸入一次。\n\n")
        # 12. 【活動結束後資料建檔】「已登記出席統計表」生成「計算完成統計表」並「輸入資料庫」"
        # "C:\Users\ricardo\Desktop\Data\0311_藍天百腦匯報名清單(登陸出席).csv"
        # Produce csv file after processing
        path, sem, semester_first, semester_second, fc, sc, date = __init__.get_information("10")
        file_source = file_management.File(path, sem, semester_first, semester_second, fc, sc, date)
        file_source.get_file()
        data_source = data_processing.Data(file_source.year,
                                          file_source.semester,
                                          file_source.file_path,
                                          file_source.first_cat,
                                          file_source.second_cat)
        data, produced_df_path = data_source.data_processing()
        file_management.remove_temp()
        print('# 成功生成CSV')
        print('# 開始將生成csv輸入資料庫...')
        # insert data into database
        file_source = file_management.File(produced_df_path, sem, semester_first, semester_second, fc, sc, date)
        file_source.get_file()
        # create a temp csv file in utf8 encoding
        data = pd_read_csv(file_source.file_path, encoding="Big5", sep=",")
        # set name of the table
        db_connection = database_management.DataConnection(data, config, fc, sc, date)
        # create new table for the data
        db_connection.create_table(db_connection.table_name)
        # insert data into mysql table
        db_connection.insert_table(db_connection.table_name)
        # create main table in mysql database
        db_connection.create_table("主資料表")
        # insert data into main mysql table
        db_connection.insert_table("主資料表")
        print("# 資料輸入資料庫成功，返回主選單")
        t_sleep(1)
        file_management.remove_temp()



