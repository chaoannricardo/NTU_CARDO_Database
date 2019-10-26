from os import remove as os_remove
from sys import exit as sys_exit


class File:
    def __init__(self, path, semester, first_cat, second_cat, date):
        self.file_path = path
        self.semester = semester
        self.semester_first = ""
        self.semester_second = ""
        self.first_cat = first_cat
        self.second_cat = second_cat
        self.date = date
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
        elif self.first_cat == "0":
            self.first_cat = input("# 請輸入本系列場次名稱: ")
        else:
            print("# 您輸入的號碼無效，程式終止")
            sys_exit(0)

    def get_file(self):
        # edit file path to read in the file
        try:
            self.file_path = self.file_path.replace("\\", "/").replace("\"", "")
            file = open(self.file_path, mode="r")
            # Collect title (activity name), and create temp_data for further processing
            temp_data = open("./temp_data.csv", mode="w+")
            for index, line in enumerate(file):
                if index == 0:
                    activity_name = line.split(",")[0]
                    print("# 目前處理活動: ", activity_name)
                else:
                    temp_data.write(line)
            file.close()
            temp_data.close()
            print("# 檔案抓取成功，程式繼續")
        except BaseException:
            print("# 檔案抓取失敗，程式繼續 ")
            print("# 您所輸入的路徑不正確或不存在，程式終止")
            sys_exit(0)


def remove_temp():
    # remove temp_data
    try:
        os_remove("./temp_data.csv")
    except:
        print("# 在工作目錄找不到暫存檔案")


if __name__ == '__main__':
    # "C:\Users\ricardo\Desktop\Data\0311_藍天百腦匯報名清單(登陸出席).csv"
    file_path = input()
    kkk = File(file_path, "107-2", "1", "藍天電腦", "2019/1/1")
    kkk.get_file()
    print(kkk.file_path)
    print(kkk.first_cat)
    remove_temp()
