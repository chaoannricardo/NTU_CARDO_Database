from pandas import read_csv as pd_read_csv
from pandas import DataFrame as pd_DataFrame
from sys import exit as sys_exit


class Data:
    def __init__(self, year, semester, file_path, first_cat, second_cat):
        Data.year = year
        Data.semester = semester
        Data.file_path = file_path
        Data.first_cat = first_cat
        Data.second_cat = second_cat

    # remember to install cryptography (pip install cryptography)
    def data_processing(self):
        print("# 資料處理開始")
        # Process remain df
        year_semester = self.year + "-" + self.semester
        try:
            df = pd_read_csv("./temp_data.csv", encoding="Big5")
            # fill-up year, semester, year_semester value
            df.loc[:, '年度'] = self.year
            df.loc[:, '學期'] = self.semester
            df.loc[:, '年度學期'] = year_semester
            cardo_points = []
            black_list_add = []
            attendance_list = []
            # calculate cardo points, and black list of each attendance
            internet_list = df.loc[:, '網路位址'].tolist()
            point_list = df.loc[:, '實體時數'].tolist()
            for i, j in enumerate(df.loc[:, '出席否'].tolist()):
                if j == '是':
                    if type(internet_list[i]) == str:
                        cardo_points.append(point_list[i])
                        black_list_add.append(0)
                        attendance_list.append("網路報名")
                    else:
                        cardo_points.append(0)
                        black_list_add.append(0)
                        attendance_list.append("現場報名")
                else:
                    cardo_points.append(0)
                    black_list_add.append(1)
                    attendance_list.append("網路報名")
            df.loc[:, '類別'] = self.first_cat
            df.loc[:, '場次'] = self.second_cat
            df.loc[:, '報名方式'] = attendance_list
            df.loc[:, 'CARDO點數'] = cardo_points
            df.loc[:, '是否計算黑名單'] = black_list_add
            split_file_path_csv = self.file_path.split(".csv")
            temp_file_path = split_file_path_csv[0] + "_已計算黑名單和CARDO點數.csv"
            df.to_csv(temp_file_path, index=None, header=True, sep=',', encoding="Big5")
            print("# 資料處理成功，輸出'_已計算黑名單和CARDO點數.csv'")
            # Process Coss-Check CSV
            temp_pivot_source = pd_DataFrame({'出席否': df.loc[:, '出席否'].tolist(),
                                              '報名方式': df.loc[:, '報名方式'].tolist()})
            confusion_matrix = temp_pivot_source.pivot_table(index='出席否',
                                                             columns='報名方式',
                                                             aggfunc=len)
            print("# 資料處理成功，列印'_出席確認表'")
            print(confusion_matrix)
        except:
            print("# 資料處理失敗，程式終止")
            print("# 您所輸入資料是否格式和以前不大一樣？請聯絡維護人員")
            sys_exit(0)
        return df
