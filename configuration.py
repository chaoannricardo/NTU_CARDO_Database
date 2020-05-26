from pymysql import cursors
from os import system as os_system
from time import sleep as t_sleep
import database_management


def clear_console():
    os_system("clear")


def print_licence():
    text = "----------------------------------------------------------------------------------\n" + \
           "程式開發者：趙上涵；Ricardo S. Chao\n" + \
           "E-mail: richiechao95@gmail.com\n" + \
           "Linkedin: https://www.linkedin.com/in/chaoannricardo/\n" + \
           "本程式 Source Code 網址：https://github.com/chaoannricardo/NTU_CARDO_Database\n" + \
           "Version: 2.0 Beta; Last Modified Date: 2020/05/11\n" + \
           "程式導覽手冊：https://github.com/chaoannricardo/NTU_CARDO_Database/blob/master/GUIDE.md\n" + \
           "----------------------------------------------------------------------------------"
    print(text)
    return text


def get_config(account, password):
    config = {
        # 'host': '127.0.0.1',
        'host': '220.133.208.39',
        # 'host': '10.181.2.122',
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
    license = print_licence()
    print("# 歡迎使用本資料庫系統")
    config = get_config(account, password)
    # 身分驗證
    print('# 登入中....')
    conn = database_management.pymysql_connect(**config)
    print("# 登入成功，歡迎回來", account)
    print()
    print()
    return config
