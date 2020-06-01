from os import remove as os_remove
from sys import exit as sys_exit
from codecs import open as codecs_open
import sys
import traceback


class File:
    def __init__(self, path, semester, semester_first, semester_second, first_cat, second_cat, date):
        self.file_path = path
        self.semester = semester
        self.semester_first = semester_first
        self.semester_second = semester_second
        self.first_cat = first_cat
        self.second_cat = second_cat
        self.date = date
        self.year = date[0:4]
        if self.first_cat == "1":
            self.first_cat = "TCP_希望種子培育計畫"
        elif self.first_cat == "2":
            self.first_cat = "TIP_企業實習計劃說明會"
        elif self.first_cat == "3":
            self.first_cat = "職涯講堂"
        elif self.first_cat == "4":
            self.first_cat = "職業工坊"
        elif self.first_cat == "5":
            self.first_cat = "菁粹會客室"

    def get_file(self):

        try:
            # edit file path to read in the file
            self.file_path = self.file_path.replace("\\", "/").replace("\"", "")
            file = codecs_open(self.file_path, 'r', encoding='big5', errors='ignore')
            # Collect title (activity name), and create temp_data for further processing
            temp_data = open("./temp_data.csv", mode="w+", encoding='big5')
            for index, line in enumerate(file):
                if index == 0:
                    activity_name = max(line.split(","), key=len)
                    print("# 目前處理", activity_name, sep="")
                else:
                    temp_data.write(line)
            file.close()
            temp_data.close()
            print("# 檔案抓取成功，程式繼續")
        except Exception as e:
            print("# 檔案抓取失敗")
            print("# 您所輸入的路徑不正確或不存在，程式終止")

            # print out error message when error occurs
            # https://dotblogs.com.tw/caubekimo/2018/09/17/145733
            error_class = e.__class__.__name__  # 取得錯誤類型
            detail = e.args[0]  # 取得詳細內容
            cl, exc, tb = sys.exc_info()  # 取得Call Stack
            lastCallStack = traceback.extract_tb(tb)[-1]  # 取得Call Stack的最後一筆資料
            fileName = lastCallStack[0]  # 取得發生的檔案名稱
            lineNum = lastCallStack[1]  # 取得發生的行號
            funcName = lastCallStack[2]  # 取得發生的函數名稱
            errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
            print(errMsg)

            sys_exit(0)


def remove_temp():
    # remove temp_data
    try:
        os_remove("./temp_data.csv")
    except Exception as e:
        print("# 在工作目錄找不到暫存檔案")