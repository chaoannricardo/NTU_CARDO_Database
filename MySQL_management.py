from numpy import int64 as np_int64
from numpy import float64 as np_float64
import pymysql
from sys import exit as sys_exit
from time import localtime
from pandas import DataFrame as pd_DataFrame


def commit(config, command):
    # Connect to MySQL Server
    while True:
        try:
            print('========== Connecting to MySQL Database.... ==========')
            conn = pymysql.connect(**config)
            cursorObject = conn.cursor()
            # Execute SQL command
            cursorObject.execute(command)
        except BaseException:
            print("========== Unable to connect to MySQL Database. ==========")
            print("================= The program has been terminated =================.")
            sys_exit(0)
            break
        else:
            print("========== Sucessfully connected, command executed ==========")
            break


def create(data, first_cat, second_cat, config):
    column_sql_dict = {
        "報名時間": "VARCHAR(32)",
        "姓名": "VARCHAR(32)",
        "身分證字號": "VARCHAR(32)",
        "性別": "VARCHAR(32)",
        "生日": "VARCHAR(32)",
        "身份別": "VARCHAR(32)",
        "一級單位": "VARCHAR(32)",
        "二級單位": "VARCHAR(32)",
        "職稱": "VARCHAR(32)",
        "聯絡電話": "VARCHAR(32)",
        "電子郵件": "VARCHAR(32)",
        "餐食": "VARCHAR(32)",
        "是否需要公務員時數": "VARCHAR(32)",
        "成績": "VARCHAR(32)",
        "合格否": "VARCHAR(32)",
        "合格證號": "VARCHAR(32)",
        "備註": "VARCHAR(32)",
        "網路位址": "VARCHAR(32)",
        "帳號": "VARCHAR(32)",
        "學位學分": "INT",
        "課程類別代碼": "VARCHAR(32)",
        "學習類別": "VARCHAR(32)",
        "上課縣市": "VARCHAR(32)",
        "期別": "VARCHAR(32)",
        "訓練總時數": "INT",
        "訓練總數單位": "VARCHAR(32)",
        "數位時數": "INT",
        "實體時數": "INT",
        "是否有實習過？": "VARCHAR(32)",
        "年度": "INT",
        "學期": "INT",
        "年度學期": "INT",
        "類別": "VARCHAR(32)",
        "場次": "VARCHAR(32)",
        "報名方式": "VARCHAR(32)",
        "CARDO點數": "INT",
        "是否計算黑名單": "VARCHAR(32)"
    }
    year = localtime().tm_year
    month = localtime().tm_mon
    day = localtime().tm_mday
    table_name = str(year) + str(month) + str(day) + "_" + first_cat + "_" + second_cat
    command = "CREATE TABLE " + table_name + " ("
    try:
        for i, j in enumerate(data.columns):
            if (i + 1) != len(data.columns):
                if j in column_sql_dict:
                    command = command + j + " " + column_sql_dict[j] + ", "
                else:
                    if type(data.iloc[0, i]) == str:
                        command = command + j + " VARCHAR(32), "
                    elif type(data.iloc[0, i]) == np_int64:
                        command = command + j + " INT, "
                    elif type(data.iloc[0, i]) == np_float64:
                        command = command + j + " INT, "
                    else:
                        print("Type not found.")
            else:
                if j in column_sql_dict:
                    command = command + j + " " + column_sql_dict[j] + ")"
                else:
                    if type(data.iloc[0, i]) == str:
                        command = command + j + " VARCHAR(32))"
                    elif type(data.iloc[0, i]) == np_int64:
                        command = command + j + " INT)"
                    elif type(data.iloc[0, i]) == np_float64:
                        command = command + j + " INT)"
                    else:
                        print("Type not found.")
        print(command)
        command(command, config)
    except:
        for i, j in enumerate(data.columns):
            if (i + 1) != len(data.columns):
                if type(data.iloc[0, i]) == str:
                    command = command + j + " VARCHAR(32),"
                elif type(data.iloc[0, i]) == np_int64:
                    command = command + j + " INT,"
                elif type(data.iloc[0, i]) == np_float64:
                    command = command + j + " INT,"
                else:
                    print("Type not found.")
            else:
                if type(data.iloc[0, i]) == str:
                    command = command + j + " VARCHAR(32))"
                elif type(data.iloc[0, i]) == np_int64:
                    command = command + j + " INT)"
                elif type(data.iloc[0, i]) == np_float64:
                    command = command + j + " INT)"
                else:
                    print("Type not found.")
        print(command)
        command(command, config)
    return table_name
