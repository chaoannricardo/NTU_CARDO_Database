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

from models import database_management
import configuration as config
# import packages finished


def blacklist_search(row_index):
    function_font_style = tkFont.Font(family="微軟正黑體", size=14, weight=tkFont.BOLD)
    row_index += 1
    configuration = config.auto_log_in()
    yes_no = blacklist_var.get()

    # test whether input is valid, if valid, activate blacklist search
    yes_no_list = ["Y", "y", "N", "n"]
    isNumber = False
    try:
        yes_no = int(yes_no)
        isNumber = True
    except ValueError:
        pass
    if yes_no not in yes_no_list and isNumber is False:
        Label(main_frame, text="所輸入錯誤，請再輸入一次",
              font=function_font_style, fg='red').grid(row=row_index, column=0, columnspan=3)
    else:
        simple_connection = database_management.SimpleConnection(configuration)
        simple_connection.black_list_search(yes_no)
        Label(main_frame, text="查詢完成！結果已輸出於桌面上\n請結束程式，或再次使用查詢功能",
              font=function_font_style, fg='red').grid(row=row_index, column=0, columnspan=3)


if __name__ == '__main__':
    # Basic Settings
    win = Tk()
    title_font_style = tkFont.Font(family="微軟正黑體", size=12)
    normal_font_style = tkFont.Font(family="微軟正黑體", size=10)
    note_font_style = tkFont.Font(family="微軟正黑體", size=8)
    blank_font_style = tkFont.Font(size=3)
    license_font_style = tkFont.Font(family="微軟正黑體", size=6)
    win.title("NTU CARDO 資料庫管理系統 - 黑名單/資料查詢")
    win.geometry("800x550+100+100")
    main_frame = Frame(win)
    main_frame.pack(side='top', fill=X, padx=20, pady=5)
    row_index = 0

    # title section
    row_index += 1
    Label(main_frame, text="\n【國立臺灣大學管理學院生涯發展中心（CARDO）資料處理及資料庫管理程式】\n ",
          font=title_font_style).grid(row=row_index, column=0, columnspan=3)

    # input sections

    # 黑名單查詢區
    blacklist_var = StringVar()
    row_index += 1
    Label(main_frame,
          text="黑名單查詢：",
          font=note_font_style).grid(row=row_index, column=0, sticky='w')

    # black list entry
    blacklist_entry = Entry(main_frame, textvariable=blacklist_var, font=title_font_style, width=10).grid(
        row=row_index,
        column=1,
        sticky='w')

    # empty column
    Label(main_frame,
          text=" ",
          font=note_font_style).grid(row=row_index, column=2, sticky='w')

    # execute button
    Button(main_frame, text="黑名單查詢", font=normal_font_style,
           bg='skyblue', width=10, height=1, command=lambda: blacklist_search(row_index)).grid(row=row_index, column=3,
                                                                                               sticky='w')

    blacklist_text = "是否只顯示進入黑名單（>=5）的同學列表？(Y/N)\n或可輸入整數以顯示黑名單次數高於輸入值的名單；\n輸入N則會顯示所有同學目前的黑名單技術，並以降冪排序： "
    for i, j in enumerate(blacklist_text.splitlines()):
        row_index += 1
        Label(main_frame,
              text=j,
              font=note_font_style).grid(row=row_index, column=0, sticky='w')

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