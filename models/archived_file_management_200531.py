from os import remove as os_remove
from sys import exit as sys_exit
from pandas import read_excel as pd_read_excel
from codecs import open as codecs_open


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
            data = pd_read_excel(self.file_path, encoding='big5', header=None)

            # collect activity name
            first_row_list = [str(j) for i, j in enumerate(data.iloc[0, :].tolist())]
            activity_name = max(first_row_list, key=len)
            print("# 目前處理： ", activity_name, sep="")

            # save current file to a utf-8 csv
            data = data.iloc[1:, :]
            data.columns = data.iloc[0, :]
            data = data.iloc[1:, :]
            data.to_csv('./temp_data_utf8.csv', encoding='utf8', index=None)

            # manage to change the encoding into big5
            # read input file
            with codecs_open('./temp_data_utf8.csv', 'r', encoding='utf8') as file:
                lines = file.read()
            # write output file
            with codecs_open('./temp_data.csv', 'w', encoding='big5') as file:
                file.write((lines.encode('big5', 'ignore').decode('big5')))

            print("# 檔案抓取成功，程式繼續")
        except:
            print("# 檔案抓取失敗")
            print("# 請檢察您所輸入的路徑，或聯絡程式管理員")
            print("# 程式終止")
            sys_exit(0)


def remove_temp():
    # remove temp_data
    try:
        os_remove("./temp_data.csv")
    except:
        print("# 在工作目錄找不到暫存檔案")


def remove_temp_utf8():
    # remove temp_data
    try:
        os_remove("./temp_data_utf8.csv")
    except:
        print("# 在工作目錄找不到暫存檔案")

