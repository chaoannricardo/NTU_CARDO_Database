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


def insert_db():
    configuration = config.auto_log_in()
    location = location_var.get()
    view_CLI.quick_insert_db(location, configuration)
    Label(main_frame, text="處理完成！", font=note_font_style).grid(row=row_now_list[0], column=0, sticky='w')


if __name__ == '__main__':
    # Basic Settings
    win = Tk()
    title_font_style = tkFont.Font(family="微軟正黑體", size=12)
    normal_font_style = tkFont.Font(family="微軟正黑體", size=10)
    note_font_style = tkFont.Font(family="微軟正黑體", size=8)
    blank_font_style = tkFont.Font(size=3)
    license_font_style = tkFont.Font(family="微軟正黑體", size=7)
    win.title("NTU CARDO 資料庫管理系統 - 資料匯入")
    win.geometry("1000x600+100+100")
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
    location_entry = Entry(main_frame, textvariable=location_var, font=normal_font_style, width=30).grid(row=row_index, column=1, sticky='w')

    # 執行紐
    Button(main_frame, text="資料處理\n並匯入資料庫", font=normal_font_style,
           bg='skyblue', width=20, height=2, command=lambda: insert_db()).grid(row=row_index, column=2,
                                                                                         sticky='w')

    # 解說文字
    row_index += 1
    Label(main_frame, text="注意事項：", font=note_font_style).grid(row=row_index, column=0, sticky='w')
    Label(main_frame, text="範例檔案格式:", font=note_font_style).grid(row=row_index, column=1, sticky='w')

    introduction_text = "1. 將從台大網站下載的'xls'檔案，\n以Excel開啟後，以'CSV (逗號分隔) (*.csv)'方式另存新檔)\n2. 輸入另存新檔後csv路徑(Shift+滑鼠右鍵 => " \
                        "複製路徑):\n**若執行期間程式停止回應，請不用擔心等待程式執行\n若資料較龐大所需時間較長"
    example_text = "請注意底線'_'為分隔符號，並請不要含有空格)\n20190314_107-2_TIP企業實習計劃說明會_精英公關.csv\n20200317_108-2_職涯講堂_" \
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

    row_now_list = [row_index]

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

    # # 空行
    # row_index += 1
    # Label(main_frame, text="", font=blank_font_style).grid(row=row_index)
    #
    # # 請輸入年度學期(EX: 106-1, 107-2):
    # row_index += 1
    # Label(main_frame, text="請輸入年度學期(EX: 106-1, 107-2):        ", font=normal_font_style).grid(row=row_index,
    #                                                                                           column=0, sticky='w')
    # sem_entry = Entry(main_frame, font=normal_font_style, width=20).grid(row=row_index, column=1, sticky='w')
    #
    # # 空行
    # row_index += 1
    # Label(main_frame, text="", font=blank_font_style).grid(row=row_index)
    #
    # # 請輸入本次系列類別:
    # row_index += 1
    # Label(main_frame, text="請輸入本次系列類別:        ", font=normal_font_style).grid(row=row_index, column=0, sticky='w')
    # tkvar = StringVar(win)
    # option_dict = {"TCP_希望種子培育計畫",
    #                "TIP_企業實習計劃說明會",
    #                "職涯講堂",
    #                "職業工坊",
    #                "菁粹會客室",
    #                "其他"}
    # tkvar.set("TIP_企業實習計劃說明會")
    # pop_menu = OptionMenu(main_frame, tkvar, *option_dict).grid(row=row_index, column=1, sticky='w')
    #
    # # 空行
    # row_index += 1
    # Label(main_frame, text="", font=blank_font_style).grid(row=row_index)
    #
    # # 請輸入本場次名:
    # row_index += 1
    # Label(main_frame, text="請輸入本次場次名: (EX: 藍天百腦匯):       ", font=normal_font_style).grid(row=row_index,
    #                                                                                           column=0, sticky='w')
    # activity_entry = Entry(main_frame, font=normal_font_style, width=20).grid(row=row_index, column=1, sticky='w')
    #
    # # 空行
    # row_index += 1
    # Label(main_frame, text="", font=blank_font_style).grid(row=row_index)
    #
    # # 請輸入'活動'日期(:
    # row_index += 1
    # Label(main_frame, text="請輸入'活動'日期(ex: 20191026):       ", font=normal_font_style).grid(row=row_index,
    #                                                                                      column=0, sticky='w')
    # date_entry = Entry(main_frame, font=normal_font_style, width=20).grid(row=row_index, column=1, sticky='w')
    #
    # # 空行
    # row_index += 1
    # Label(main_frame, text="", font=blank_font_style).grid(row=row_index)
    #
    # # 備註欄:
    # row_index += 1
    # Label(main_frame, text="備註欄:(若無需要請留空白)        ", font=normal_font_style).grid(row=row_index, column=0,
    #                                                                               sticky='w')
    # other_entry = Entry(main_frame, font=normal_font_style, width=20).grid(row=row_index, column=1, sticky='w')
    #
    # # 空行
    # row_index += 1
    # Label(main_frame, text="", font=blank_font_style).grid(row=row_index)
    # row_index += 1
    # Label(main_frame, text="", font=blank_font_style).grid(row=row_index)

    # # buttons
    # # 標準功能
    # row_index += 1
    # Button(main_frame, text="1. 已登記出席統計表」生成「計算完成統計表」\n"
    #                         "並「輸入資料庫」（標準流程）", font=normal_font_style,
    #        bg='skyblue', width=40, height=2, command=lambda: function_1(row_index)).grid(row=row_index, column=0, sticky='w')
    #
    # # 生成表功能
    # Button(main_frame, text="2. 「已登記出席統計表」生成「計算完成統計表」\n（+ 黑名單、CARDO點數、報名方式等)",
    #        font=normal_font_style,
    #        bg='skyblue', width=40, height=2, command=lambda: function_2()).grid(row=row_index, column=1, sticky='w')
    #
    # # 空行
    # row_index += 1
    # Label(main_frame, text="", font=blank_font_style).grid(row=row_index)
    #
    # # 表輸入功能
    # row_index += 1
    # Button(main_frame, text="3. 「計算完成統計表」「輸入資料庫」", font=normal_font_style,
    #        bg='skyblue', width=40, height=2, command=lambda: function_3()).grid(row=row_index, column=0, sticky='w')
    #
    # # 空行
    # row_index += 1
    # Label(main_frame, text="", font=blank_font_style).grid(row=row_index)
    # row_index += 1
    # Label(main_frame, text="", font=blank_font_style).grid(row=row_index)

    # activate the app
    win.mainloop()
