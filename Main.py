# import packages needed
from os import listdir as os_lisdir
from os import system as os_system
from pymysql import cursors
from sys import exit as sys_exit
from time import sleep as t_sleep
import DataProcessing
import FileManagement
import DatabaseManagement

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'user',
    'password': 'password',
    'db': 'cardo',
    'charset': 'utf8mb4',
    'cursorclass': cursors.DictCursor,
}


def get_information():
    path = input(
        "【注意事項】\n請將從台大網站下載的'xls'檔案，以Excel開啟後，以'CSV (逗號分隔) (*.csv)'方式另存新檔)\n請輸入另存新檔後csv路徑(Shift+滑鼠右鍵 => 複製路徑): ")
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
            "# 請輸入本次系列號碼:\n    1:TCP_希望種子培育計畫\n    2:TIP_企業實習計劃說明會\n    3:職涯講堂\n    4:職業工坊\n    5:菁粹會客室\n    0:自行輸入\n# 請輸入:  ")
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


def get_information_finished():
    path = input(
        "【注意事項】\n請輸入'經過本程式處理過後生成的「計算完成統計表」'csv路徑(Shift+滑鼠右鍵 => 複製路徑): ")
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
            "# 請輸入本次系列號碼:\n    1:TCP_希望種子培育計畫\n    2:TIP_企業實習計劃說明會\n    3:職涯講堂\n    4:職業工坊\n    5:菁粹會客室\n    0:自行輸入\n# 請輸入:  ")
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
    print("【國立臺灣大學 CARDO 資料處理及資料庫管理程式】")
    print("# 功能選單：")
    print("# 0. 【離開】程式結束")
    print()
    print("# 【活動結束後資料建檔】")
    print("# 1. 【活動結束後資料建檔】「已登記出席統計表」生成「計算完成統計表」（+ 黑名單、CARDO點數、報名方式等)")
    print("# 2. 【活動結束後資料建檔】「計算完成統計表」「輸入資料庫」")
    print("# 3. 【活動結束後資料建檔】「已登記出席統計表」生成「計算完成統計表」並「輸入資料庫」")
    print()
    print("# 【黑名單管理】")
    print("# 4. 【黑名單管理】查詢目前進入黑名單的同學名單")
    print("# 5. 【黑名單管理】黑名單生效")
    print("# 6. 【資料庫查詢】以姓名查詢參加CARDO活動紀錄")
    print()
    print("【額外功能】")
    print()
    print("# 7. 【快速建檔】過去手工歷史「計算完成統計表」「輸入資料庫」")


def clear_console():
    clear = lambda: os_system("cls")
    clear()


# "C:\Users\ricardo\Desktop\Data\0311_藍天百腦匯報名清單(登陸出席).csv"
# Process Starts
if __name__ == '__main__':
    while True:
        get_menu()
        while True:
            command = input("# 請輸入想要使用的功能代碼： ")
            if command not in ["0", "1", "2", "3"]:
                print("# 您輸入的功能代碼不正確，請再輸入一次，或輸入0終止程式")
            else:
                break
        if command == "0":
            print("# 程式結束，謝謝您的使用")

            sys_exit(0)
        elif command == "1":
            # 1. 【活動結束後資料建檔】「已登記出席統計表」生成「計算完成統計表」（+ 黑名單、CARDO點數、報名方式等)
            # Produce csv file after processing
            path, sem, semester_first, semester_second, fc, sc, date = get_information()
            file_source = FileManagement.File(path, sem, semester_first, semester_second, fc, sc, date)
            file_source.get_file()
            data_source = DataProcessing.Data(file_source.year,
                                              file_source.semester,
                                              file_source.file_path,
                                              file_source.first_cat,
                                              file_source.second_cat)
            data = data_source.data_processing()
            FileManagement.remove_temp()
            print('# 成功生成CSV')
            print('# 返回主選單')
            t_sleep(3)
            clear_console()
        elif command == "2":
            # 2. 【活動結束後資料建檔】「計算完成統計表」「輸入資料庫」
            print("# 功能尚未完成建置")
            t_sleep(3)
            clear_console()
        elif command == "3":
            # 3. 【活動結束後資料建檔】「已登記出席統計表」生成「計算完成統計表」並「輸入資料庫」"
            # Produce csv file after processing
            path, sem, semester_first, semester_second, fc, sc, date = get_information()
            file_source = FileManagement.File(path, sem, semester_first, semester_second, fc, sc, date)
            file_source.get_file()
            data_source = DataProcessing.Data(file_source.year,
                                              file_source.semester,
                                              file_source.file_path,
                                              file_source.first_cat,
                                              file_source.second_cat)
            data = data_source.data_processing()
            FileManagement.remove_temp()
            print('# 成功生成CSV')
            print('# 返回主選單')
            # Insert into MySQL Database
            # database_source = DatabaseManagement.DatabaseConnection(data, config, file_source.first_cat, file_source.second_cat, date)
            # database_source.create()
        elif command == "4":
            print("本功能尚未開通")
        elif command == "5":
            print("本功能尚未開通")
        elif command == "6":
            print("本功能尚未開通")
        elif command == "7":
            # 7. 【快速建檔】過去手工歷史「計算完成統計表」「輸入資料庫」
            print("# 請輸入放置過去手工歷史「計算完成統計表」資料夾")
            print("# ''''重要''''")
            print("# ")
            os_lisdir()
