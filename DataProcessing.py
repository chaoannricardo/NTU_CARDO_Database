from pandas import read_csv as pd_read_csv
from pandas import DataFrame as pd_DataFrame
from sys import exit as sys_exit


# remember to install cryptography (pip install cryptography)
def data_processing(year, semester, file_path, first_cat, second_cat):
    print("# 資料處理開始")
    # Process remain data
    year_semester = year + "-" + semester
    try:
        data = pd_read_csv("./temp_data.csv", encoding="Big5")
        # fill-up year, semester, year_semester value
        data.loc[:, '年度'] = year
        data.loc[:, '學期'] = semester
        data.loc[:, '年度學期'] = year_semester
        cardo_points = []
        black_list_add = []
        attendance_list = []
        # calculate cardo points, and black list of each attendance
        internet_list = data.loc[:, '網路位址'].tolist()
        point_list = data.loc[:, '實體時數'].tolist()
        for i, j in enumerate(data.loc[:, '出席否'].tolist()):
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
        data.loc[:, '類別'] = first_cat
        data.loc[:, '場次'] = second_cat
        data.loc[:, '報名方式'] = attendance_list
        data.loc[:, 'CARDO點數'] = cardo_points
        data.loc[:, '是否計算黑名單'] = black_list_add
        split_file_path_csv = file_path.split(".csv")
        temp_file_path = split_file_path_csv[0] + "_已計算黑名單和CARDO點數.csv"
        data.to_csv(temp_file_path, index=None, header=True, sep=',', encoding="Big5")
        print("# 資料處理成功，輸出'_已計算黑名單和CARDO點數.csv'")
        # Process Coss-Check CSV
        temp_pivot_source = pd_DataFrame({'出席否': data.loc[:, '出席否'].tolist(),
                                          '報名方式': data.loc[:, '報名方式'].tolist()})
        confusion_matrix = temp_pivot_source.pivot_table(index='出席否',
                                                         columns='報名方式',
                                                         aggfunc=len)
        print("# 資料處理成功，列印'_出席確認表'")
        print(confusion_matrix)
        return data
    except:
        print("# 資料處理失敗，程式終止")
        print("# 您所輸入資料是否格式和以前不大一樣？請聯絡維護人員")
        sys_exit(0)