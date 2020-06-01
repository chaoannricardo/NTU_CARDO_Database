# -*- coding: utf8 -*-
from pymysql import cursors
from sys import exit as sys_exit
from time import sleep as t_sleep
from models import database_management
from pandas import DataFrame as pd_DataFrame
import pymysql


def print_licence():
    text = "----------------------------------------------------------------------------------\n" + \
           "程式開發者：趙上涵；Ricardo S. Chao\n" + \
           "E-mail: richiechao95@gmail.com\n" + \
           "Linkedin: https://www.linkedin.com/in/chaoannricardo/\n" + \
           "本程式 Source Code 網址：https://github.com/chaoannricardo/NTU_CARDO_Database\n" + \
           "Version: 2.0 Beta; Last Modified Date: 2020/05/27\n" + \
           "程式導覽手冊：https://github.com/chaoannricardo/NTU_CARDO_Database/blob/master/GUIDE.md\n" + \
           "----------------------------------------------------------------------------------"
    print(text)
    return text


def get_config(account, password):
    config = {
        'host': '10.181.2.122',
        'port': 3306,
        'user': account,
        'password': password,
        'db': 'cardo',
        'charset': 'utf8mb4',
        'cursorclass': cursors.DictCursor,
    }
    return config


def get_config_develop(account, password):
    config = {
        'host': '220.133.208.39',
        'port': 3306,
        'user': account,
        'password': password,
        'db': 'cardo',
        'charset': 'utf8mb4',
        'cursorclass': cursors.DictCursor,
    }
    return config


def auto_log_in():
    account = 'cardo'
    password = 'ntucardo'
    print("----------------------------------------------------------------------------------")
    print("【國立臺灣大學管理學院生涯發展中心（CARDO）資料處理及資料庫管理程式】")
    print_licence()
    print("# 歡迎使用本資料庫系統")
    try:
        config = get_config(account, password)
        # 身分驗證
        print('# 登入中....')
        conn = database_management.pymysql_connect(**config)
    except: # for development
        config = get_config_develop(account, password)
        # 身分驗證
        print('# 登入中....')
        conn = database_management.pymysql_connect(**config)
    print("# 登入成功，歡迎回來", account, '\n\n')
    return config


def get_main_frame_dict():
    main_frame_dict = {
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
        "備註": "longtext",
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
        "年度": "INT",  # 此欄由程式自動輸出
        "學期": "INT",  # 此欄由程式自動輸出
        "年度學期": "VARCHAR(100)",  # 此欄由程式自動輸出
        "類別": "VARCHAR(100)",  # 此欄由程式自動輸出
        "場次": "VARCHAR(100)",  # 此欄由程式自動輸出
        "報名方式": "VARCHAR(100)",  # 此欄由程式自動輸出
        "CARDO點數": "INT",  # 此欄由程式自動輸出
        "是否計算黑名單": "INT",  # 此欄由程式自動輸出
        # 以下為常見問答問題，記得標點符號等所有字符都必須一樣，否則將會被視為不同欄位
        "參加本基礎課程的原因？": "longtext",
        "申請動機": "longtext",
        "描述我的個人特質": "longtext",
        "是否有實習過？": "longtext",
        "使用U Meeting或現場參加": "longtext",
        "想問主講者的問題": "longtext",
        "想問主講者的問題？": "longtext",
        "想問學長姊的問題？": "longtext"
    }
    return main_frame_dict


def get_db_number_list():
    number_list = ["學位學分",
                   "訓練總時數",
                   "數位時數",
                   "實體時數",
                   "年度",
                   "學期",
                   "CARDO點數",
                   "是否計算黑名單"]
    return number_list


# depreciated, use auto_login() instead
def log_in():
    while True:
        print("----------------------------------------------------------------------------------")
        print("【國立臺灣大學管理學院生涯發展中心（CARDO）資料處理及資料庫管理程式】")
        print_licence()
        print("# 歡迎使用本資料庫系統")
        account = input("# 請輸入使用者帳號，或輸入'exit'離開本程式： ")
        if account == "exit":
            print("# 謝謝您的使用，歡迎下次光臨。")
            t_sleep(1)
            sys_exit(0)  # terminate program if input exit
        else:
            # enter password
            password = input("# 請輸入使用者密碼： ")
            try:
                config = get_config(account, password)
                # 身分驗證
                print('# 登入中....')
                database_management.pymysql_connect(**config)
                print("# 登入成功，歡迎回來", account, '\n\n')
                t_sleep(1)
                break
            except pymysql.err.OperationalError:
                print("# 您輸入的帳號或密碼錯誤，請再輸入一次。\n\n")
    return config


if __name__ == '__main__':
    configuration_dict = get_main_frame_dict()
    column_df = pd_DataFrame({
        '欄位名': ['# 此為主資料表裡有的欄位名稱，\n如想新增不同的欄位，請洽程式維護者'] + list(configuration_dict.keys()),
    })
    column_df.to_csv('./column_list.csv', sep=',', index=False, encoding='big5')