# import packages needed
from pymysql import cursors
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
        option_list = ["1", "2", "3", "4", "5"]
        if fc == "0":
            fc = input("# 請輸入本系列場次名稱: ")
            break
        elif fc not in option_list:
            print("# 您輸入的號碼無效，請再輸入一次")
        else:
            break
    sc = input("# 請輸入本次場次名: (EX: 藍天百腦匯):  ")
    date = input("# 請輸入'活動'日期(ex: 20191026):  ")
    return path, sem, semester_first, semester_second, fc, sc, date


def raw_data_processing():
    path, sem, semester_first, semester_second, fc, sc, date = get_information()
    loaded_file = FileManagement.File(path, sem, semester_first, semester_second, fc, sc, date)
    loaded_file.get_file()
    DataProcessing.data_processing(loaded_file.semester_first, loaded_file.semester_second, loaded_file.file_path, loaded_file.first_cat, loaded_file.second_cat)
    FileManagement.remove_temp()


# "C:\Users\ricardo\Desktop\Data\0311_藍天百腦匯報名清單(登陸出席).csv"
# Process Starts
if __name__ == '__main__':
    print("【國立臺灣大學 CARDO 資料處理及資料庫管理程式】")
    print("")
    command = input()
    if command == "1":
        print()

