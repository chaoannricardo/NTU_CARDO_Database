from pymysql import cursors
from os import system as os_system
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
        "是否計算黑名單": "VARCHAR(100)",
        "參加本基礎課程的原因？": "longtext"
    }
    return main_frame_dict


def get_db_number_list():
    number_list = ["學位學分",
                   "訓練總時數",
                   "數位時數",
                   "實體時數",
                   "年度",
                   "學期",
                   "CARDO點數"]
    return number_list

