# -*- coding: utf8 -*-
# import packages needed
from tkinter import *
from pymysql import cursors
import tkinter.font as tkFont

# import configuration in parent dir
import os, sys, inspect, view_CLI

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import configuration as config
# import packages finished


def insert_db(row_index):
    function_font_style = tkFont.Font(family="微軟正黑體", size=14, weight=tkFont.BOLD)
    row_index += 1
    configuration = config.auto_log_in()
    location = location_var.get()
    view_CLI.quick_insert_db(location, configuration)
    Label(main_frame, text="處理完成！\n出席對照表列印於終端機上！\n已計算黑名單和CARDO點數.csv & 出席確認表皆已匯出成功！\n請輸入下個檔案路徑繼續執行程式",
          font=function_font_style, fg='red').grid(row=row_index, column=0, columnspan=3)


if __name__ == '__main__':
    # Basic Settings
    win = Tk()
    title_font_style = tkFont.Font(family="微軟正黑體", size=12)
    normal_font_style = tkFont.Font(family="微軟正黑體", size=10)
    note_font_style = tkFont.Font(family="微軟正黑體", size=8)
    blank_font_style = tkFont.Font(size=3)
    license_font_style = tkFont.Font(family="微軟正黑體", size=7)
    win.title("NTU CARDO 資料庫管理系統 - 資料匯入")
    win.geometry("1000x550+100+100")
    main_frame = Frame(win)
    main_frame.pack(side='top', fill=X, padx=20, pady=5)
    row_index = 0

    # title section
    row_index += 1
    Label(main_frame, text="\n【國立臺灣大學管理學院生涯發展中心（CARDO）資料處理及資料庫管理程式】\n ",
          font=title_font_style).grid(row=row_index, column=0, columnspan=3)

    # input sections

    # 資料庫匯入區
    # 請輸入欲匯入/處理的檔案位置
    location_var = StringVar()
    row_index += 1
    Label(main_frame, text="請輸入欲匯入/處理的檔案位置：", font=normal_font_style).grid(row=row_index, column=0, sticky='w')
    location_entry = Entry(main_frame, textvariable=location_var, font=normal_font_style, width=30).grid(row=row_index,
                                                                                                         column=1,
                                                                                                         sticky='w')

    # 執行紐
    Button(main_frame, text="資料處理\n並匯入資料庫", font=normal_font_style,
           bg='skyblue', width=20, height=2, command=lambda: insert_db(row_index)).grid(row=row_index, column=2,
                                                                                        sticky='w')

    # 解說文字
    row_index += 1
    Label(main_frame, text="注意事項：", font=note_font_style).grid(row=row_index, column=0, sticky='w')
    Label(main_frame, text="範例檔案格式:", font=note_font_style).grid(row=row_index, column=1, sticky='w')

    introduction_text = "1. 將從台大網站下載的'xls'檔案，\n以Excel開啟後，以'CSV (逗號分隔) (*.csv)'方式另存新檔)\n2. 輸入另存新檔後csv路徑(Shift+滑鼠右鍵 => " \
                        "複製路徑):\n**若執行期間程式停止回應，請不用擔心等待程式執行\n若資料較龐大所需時間較長\nUI平均處理時間為90秒，請耐心等候或改使用CLI模式"
    example_text = "請注意底線'_'為分隔符號，並請不要含有空格)\n檔名格式為：日期8碼_年度-學期_場次系列名_場次名.csv\n20190314_107-2_TIP企業實習計劃說明會_精英公關.csv" \
                   "\n20200317_108-2_職涯講堂_" \
                   "學術生涯分享會-關於博士這條路.csv "

    example_text_list = example_text.splitlines()
    for i, j in enumerate(introduction_text.splitlines()):
        row_index += 1
        Label(main_frame,
              text=j,
              font=note_font_style).grid(row=row_index, column=0, sticky='w')
        try:
            Label(main_frame,
                  text=example_text_list[i],
                  font=note_font_style).grid(row=row_index, column=1, sticky='w')
        except IndexError:
            pass

    # Licence
    # 空行
    for i in range(0, 3):
        row_index += 1
        Label(main_frame, text="", font=blank_font_style).grid(row=row_index)

    license_text = config.print_licence()
    license_text_list = license_text.splitlines()
    for i, j in enumerate(license_text_list):
        row_index += 1
        Label(main_frame, text=j,
              font=license_font_style).grid(row=row_index, column=0, sticky='w')

    # activate the app
    win.mainloop()