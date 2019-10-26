from os import remove as os_remove
from sys import exit as sys_exit


class File:
    def __init__(self, file_path, semester, first_cat, second_cat, date):
        self.file_path = file_path
        self.semester = semester
        self.first_cat = first_cat
        self.second_cat = second_cat
        self.date = date

    def get_file(self):
        # edit file path to read in the file
        try:
            file_path = self.file_path.replace("\\", "/").replace("\"", "")
            file = open(file_path, mode="r")
            split_file_path = file_path.split("/")
            # Collect title (activity name), and create temp_data for further processing
            temp_data = open("./temp_data.csv", mode="w+")
            for index, line in enumerate(file):
                if index == 0:
                    activity_name = line.split(",")[0]
                    # Extract 1st Category
                    first_cat = line.split(" ")[-1].split(",")[0]
                    # Extract 2nd Category
                    second_cat = line.split("】")[1].split("/")[0]
                    print("目前處理活動: ", activity_name)
                else:
                    temp_data.write(line)
            file.close()
            temp_data.close()
            print("========== 檔案抓取成功，程式繼續 ==========")
            return file_path, first_cat, second_cat
        except BaseException:
            print("========== 檔案抓取失敗，程式繼續 ==========")
            print("您所輸入的路徑不正確或不存在，程式終止")
            sys_exit(0)

    def get_real_first_cat(self):
        if self.first_cat == "1":
            self.first_cat = ""
        elif self.first_cat == "2":
            self.first_cat = ""
        elif self.first_cat == "3":
            self.first_cat == ""
        elif self.first_cat == "4":
            self.first_cat == ""
        elif self.first_cat == "0":
            self.first_cat = input("請輸入本系列場次名稱")
        else:
            print("# 您輸入的指令無效，程式終止")
            sys_exit(0)


def remove_temp():
    # remove temp_data
    try:
        os_remove("./temp_data.csv")
    except:
        print("Could not find temp file, program exit.")
