# -*- coding: utf8 -*-
# import packages needed
from os import listdir as os_listdir
from pandas import read_csv as pd_read_csv
from sys import exit as sys_exit
from time import sleep as t_sleep
from models import data_processing, database_management, file_management
import configuration as conf


def get_information(command):
    # print out different messages depends on the input commands
    if command == "10":
        path = input(
            "【注意事項】\n請將從台大網站下載的'xls'檔案，以Excel開啟後，以'CSV (逗號分隔) (*.csv)'方式另存新檔)\n請輸入另存新檔後csv路徑(Shift+滑鼠右鍵 => 複製路徑): ")
    elif command == "11":
        print("【注意事項】\n輸入的檔案必須是與經過本程式處理過後所輸出之「計算完成統計表」擁有相同的格式。\n"
              "此功能並不接受其他格式的檔案")
        path = input("請輸入「計算完成統計表」路徑： ")
    while True:
        sem = input("# 請輸入年度學期(EX: 106-1, 107-2, 108-1....):  ")
        temp_list = sem.split("-")
        semester_first = ""
        semester_second = ""
        if len(temp_list) != 2:
            print("# 您輸入的學期格式錯誤，請再輸入一次")
        else:
            for i, j in enumerate(temp_list):
                if i == 0:
                    semester_first = j
                elif i == 1:
                    semester_second = j
            break
    while True:
        fc = input(
            "# 請輸入本次系列號碼:\n    1:TCP_希望種子培育計畫\n    2:TIP_企業實習計劃說明會\n    3:職涯講堂\n    4:職業工坊\n    5:菁粹會客室\n    "
            "0:自行輸入\n# 請輸入:  ")
        option_dict = {
            "1": "TCP_希望種子培育計畫",
            "2": "TIP_企業實習計劃說明會",
            "3": "職涯講堂",
            "4": "職業工坊",
            "5": "菁粹會客室"
        }
        if fc == "0":
            fc = input("請自行輸入本次系列活動名稱： ")
            break
        elif fc not in option_dict.keys():
            print("# 您輸入的號碼無效，請再輸入一次")
        else:
            fc = option_dict[fc]
            break
    sc = input("# 請輸入本次場次名: (EX: 藍天百腦匯):  ")
    while True:
        date = input("# 請輸入'活動'日期(ex: 20191026):  ")
        if len(date) == 8:
            try:
                date = int(date)
                date = str(date)
                break
            except:
                print("# 您所輸入的時間格式不正確，請再輸入一次")
        else:
            print("# 您所輸入的時間格式不正確，請再輸入一次")
    return path, sem, semester_first, semester_second, fc, sc, date


def get_menu():
    print("# 功能選單：")
    print("# 0. 【離開】程式結束")
    print()
    print("# 【活動結束後資料建檔】")
    print("# 10. 【活動結束後資料建檔】「已登記出席統計表」生成「計算完成統計表」（+ 黑名單、CARDO點數、報名方式等)")
    print("# 11. 【活動結束後資料建檔】「計算完成統計表」「輸入資料庫」")
    print("# 12. 【活動結束後資料建檔】「已登記出席統計表」生成「計算完成統計表」並「輸入資料庫」（標準流程）")
    print()
    print("# 【黑名單管理】(系列功能仍在建置中)")
    print("# 20. 【黑名單管理】計算黑名單")
    print("# 21. 【黑名單管理】黑名單生效")
    print("# 22. 【資料庫查詢】以姓名查詢參加CARDO活動紀錄")
    print()
    print("【額外功能】")
    print()
    print("# 90. 【快速建檔】過去手工歷史「計算完成統計表」「輸入資料庫」")


# "C:\Users\ricardo\Storage\Github\Data\0311_藍天百腦匯報名清單(登陸出席).csv"
# Process Starts
if __name__ == '__main__':
    config = conf.auto_log_in()
    # config = conf.log_in()
    while True:
        get_menu()
        while True:
            command = input("# 請輸入想要使用的功能代碼： ")
            if command not in ["0", "10", "11", "12", "20", "21", "22", "90", "admin"]:
                print("# 您輸入的功能代碼不正確，請再輸入一次，或輸入0終止程式")
            else:
                break
        if command == "0":
            print("# 程式結束，謝謝您的使用")
            sys_exit(0)
        elif command == "10":
            # 10. 【活動結束後資料建檔】「已登記出席統計表」生成「計算完成統計表」（+ 黑名單、CARDO點數、報名方式等)
            # "C:\Users\ricardo\Desktop\Data\0311_藍天百腦匯報名清單(登陸出席).csv"
            # Produce csv file after processing
            path, sem, semester_first, semester_second, fc, sc, date = get_information("10")
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
            print('# 返回主選單')
            t_sleep(1)

        elif command == "11":
            # 11. 【活動結束後資料建檔】「計算完成統計表」「輸入資料庫」
            # "C:\Users\ricardo\Desktop\Data\0311_藍天百腦匯報名清單(登陸出席)_已計算黑名單和CARDO點數.csv"
            path, sem, semester_first, semester_second, fc, sc, date = get_information("11")
            file_source = file_management.File(path, sem, semester_first, semester_second, fc, sc, date)
            file_source.get_file()
            # create a temp csv file in utf8 encoding
            data = pd_read_csv(file_source.file_path, encoding="Big5", sep=",")
            # set name of the table
            db_connection = database_management.DataConnection(data, config, fc, sc, date)
            # create new table for the data
            db_connection.create_table(db_connection.table_name)
            '''
            To tackle 'The MySQL server is running with the --secure-file-priv option so it cannot execute this statement' error
            reference: https://blog.csdn.net/fdipzone/article/details/78634992
            '''
            # insert data into mysql table
            db_connection.insert_table(db_connection.table_name)
            # insert data into main mysql table
            db_connection.insert_table("主資料表")
            db_connection.insert_table("黑名單統計表")
            print("# 資料輸入資料庫成功，返回主選單")
            t_sleep(1)
            file_management.remove_temp()

        elif command == "12":
            # 12. 【活動結束後資料建檔】「已登記出席統計表」生成「計算完成統計表」並「輸入資料庫」"
            # "C:\Users\ricardo\Desktop\Data\0311_藍天百腦匯報名清單(登陸出席).csv"
            # Produce csv file after processing
            path, sem, semester_first, semester_second, fc, sc, date = get_information("10")
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
            # set name of the table
            db_connection = database_management.DataConnection(data, config, fc, sc, date)
            # create new table for the data
            db_connection.create_table(db_connection.table_name)
            '''
            To tackle 'The MySQL server is running with the --secure-file-priv option so it cannot execute this statement' error
            reference: https://blog.csdn.net/fdipzone/article/details/78634992
            '''
            # insert data into mysql table
            db_connection.insert_table(db_connection.table_name)
            # insert data into main mysql table
            db_connection.insert_table("主資料表")
            db_connection.insert_table("黑名單統計表")
            print("# 資料輸入資料庫成功，返回主選單")
            t_sleep(1)
            file_management.remove_temp()

        elif command == "20":
            # 20. 【黑名單管理】計算黑名單
            simple_connection = database_management.SimpleConnection(config)
            simple_connection.black_list_search()
            print("# 黑名單列表產生完成，1秒後返回主選單")
            t_sleep(1)

        elif command == "21":
            # 21. 【黑名單管理】黑名單生效
            print("本功能尚未開通")
        elif command == "22":
            # 22. 【資料庫查詢】以姓名查詢參加CARDO活動紀錄
            print("本功能尚未開通")
        elif command == "90":
            # 90. 【快速建檔】過去手工歷史「計算完成統計表」「輸入資料庫」
            print("# 請輸入放置過去手工歷史「計算完成統計表」資料夾")
            print("# ''''重要''''")
            print("# ")
            os_listdir()