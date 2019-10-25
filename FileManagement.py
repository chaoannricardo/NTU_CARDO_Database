from os import remove as os_remove
from sys import exit as sys_exit

def get_file(file_path):
    # edit file path to read in the file
    try:
        file_path = file_path.replace("\\", "/").replace("\"", "")
        file = open(file_path, mode="r")
        split_file_path = file_path.split("/")
        output_path = ""
        #for i, j in enumerate(split_file_path):
        #    if i == (len(file_path) - 1):
        #        break
        #    output_path = output_path + j + "/"
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
    except:
        print("========== 檔案抓取失敗，程式繼續 ==========")
        print("您所輸入的路徑不正確或不存在，程式終止")
        sys_exit(0)

def remove_temp():
    # remove temp_data
    try:
        os_remove("./temp_data.csv")
    except:
        print("Could not find temp file, program exit.")