# import packages needed
from pymysql import cursors
from sys import exit as sys_exit
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


# "C:\Users\ricardo\Desktop\Data\0311_藍天百腦匯報名清單(登陸出席).csv"
# Process Starts
if __name__ == '__main__':
    while True:
        print("【國立臺灣大學 CARDO 資料處理及資料庫管理程式】")
        print("# 功能選單：")
        print("# 0. 【離開】程式結束")
        print("# 1. 【活動結束後資料建檔】出席統計表輸入資料庫，生成CSV")
        print("# 2. 【黑名單管理】查詢目前進入黑名單的同學名單")
        print("# 3. 【黑名單管理】黑名單生效")
        print("# 4. 【資料庫查詢】以姓名查詢參加CARDO活動紀錄")
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
            # 1. 活動結束：出席統計表輸入資料庫
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
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
            # Insert into MySQL Database
            # database_source = DatabaseManagement.DatabaseConnection(data, config, file_source.first_cat, file_source.second_cat, date)
            # database_source.create()
        elif command == "2":
            print("建置中")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        elif command == "3":
            print("建置中")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
