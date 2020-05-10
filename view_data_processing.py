from tkinter import *
from pymysql import cursors
import tkinter.font as tkFont
import config


def function_1(row_index):
    # 【活動結束後資料建檔】「已登記出席統計表」生成「計算完成統計表」並「輸入資料庫」
    # "C:\Users\ricardo\Desktop\Data\0311_藍天百腦匯報名清單(登陸出席).csv"
    # Produce csv file after processing
    # path, sem, semester_first, semester_second, fc, sc, date = get_information("10")
    # 訊息框
    path = location_entry.get()
    sem = str(sem_entry.get())
    temp_list = sem.split("-")
    semester_first = ""
    semester_second = ""
    if len(temp_list) != 2:
        row_index += 1
        message_label = Label(main_frame, text="# 您輸入的學期格式錯誤，請重新執行", font=normal_font_style,
                              fg='red').grid(row=row_index, column=0, sticky='w')
    else:
        for i, j in enumerate(temp_list):
            if i == 0:
                semester_first = j
            elif i == 1:
                semester_second = j


def function_2():
    pass


def function_3():
    pass





if __name__ == '__main__':
    win = Tk()
    title_font_style = tkFont.Font(family="微軟正黑體", size=12)
    normal_font_style = tkFont.Font(family="微軟正黑體", size=10)
    note_font_style = tkFont.Font(family="微軟正黑體", size=8)
    blank_font_style = tkFont.Font(size=3)
    win.title("NTU CARDO 資料庫管理系統 - 資料匯入")
    win.geometry("800x600+100+100")
    main_frame = Frame(win)
    main_frame.pack(side='top', fill=X, padx=20, pady=5)
    row_index = 0

    # title section
    row_index += 1
    Label(main_frame, text="\n【國立臺灣大學管理學院生涯發展中心（CARDO）資料處理及資料庫管理程式】\n ",
          font=title_font_style).grid(row=row_index, column=0, columnspan=2)

    # input sections
    # 請輸入欲匯入/處理的檔案位置
    row_index += 1
    Label(main_frame, text="請輸入欲匯入/處理的檔案位置：", font=normal_font_style).grid(row=row_index, column=0, sticky='w')
    location_entry = Entry(main_frame, font=normal_font_style, width=50).grid(row=row_index, column=1, sticky='w')
    row_index += 1
    Label(main_frame, text="注意事項：", font=note_font_style).grid(row=row_index, sticky='w')
    row_index += 1
    Label(main_frame, text="請將從台大網站下載的'xls'檔案，以Excel開啟後，以'CSV (逗號分隔) (*.csv)'方式另存新檔)",
          font=note_font_style).grid(row=row_index, sticky='w')
    Label(main_frame, text="請輸入另存新檔後csv路徑(Shift+滑鼠右鍵 => 複製路徑): ",
          font=note_font_style).grid(row=row_index, column=1, sticky='w')

    # 空行
    row_index += 1
    Label(main_frame, text="", font=blank_font_style).grid(row=row_index)

    # 請輸入年度學期(EX: 106-1, 107-2):
    row_index += 1
    Label(main_frame, text="請輸入年度學期(EX: 106-1, 107-2):        ", font=normal_font_style).grid(row=row_index,
                                                                                              column=0, sticky='w')
    sem_entry = Entry(main_frame, font=normal_font_style, width=20).grid(row=row_index, column=1, sticky='w')

    # 空行
    row_index += 1
    Label(main_frame, text="", font=blank_font_style).grid(row=row_index)

    # 請輸入本次系列類別:
    row_index += 1
    Label(main_frame, text="請輸入本次系列類別:        ", font=normal_font_style).grid(row=row_index, column=0, sticky='w')
    tkvar = StringVar(win)
    option_dict = {"TCP_希望種子培育計畫",
                   "TIP_企業實習計劃說明會",
                   "職涯講堂",
                   "職業工坊",
                   "菁粹會客室",
                   "其他"}
    tkvar.set("TIP_企業實習計劃說明會")
    pop_menu = OptionMenu(main_frame, tkvar, *option_dict).grid(row=row_index, column=1, sticky='w')

    # 空行
    row_index += 1
    Label(main_frame, text="", font=blank_font_style).grid(row=row_index)

    # 請輸入本場次名:
    row_index += 1
    Label(main_frame, text="請輸入本次場次名: (EX: 藍天百腦匯):       ", font=normal_font_style).grid(row=row_index,
                                                                                              column=0, sticky='w')
    activity_entry = Entry(main_frame, font=normal_font_style, width=20).grid(row=row_index, column=1, sticky='w')

    # 空行
    row_index += 1
    Label(main_frame, text="", font=blank_font_style).grid(row=row_index)

    # 請輸入'活動'日期(:
    row_index += 1
    Label(main_frame, text="請輸入'活動'日期(ex: 20191026):       ", font=normal_font_style).grid(row=row_index,
                                                                                         column=0, sticky='w')
    date_entry = Entry(main_frame, font=normal_font_style, width=20).grid(row=row_index, column=1, sticky='w')

    # 空行
    row_index += 1
    Label(main_frame, text="", font=blank_font_style).grid(row=row_index)

    # 備註欄:
    row_index += 1
    Label(main_frame, text="備註欄:(若無需要請留空白)        ", font=normal_font_style).grid(row=row_index, column=0,
                                                                                  sticky='w')
    other_entry = Entry(main_frame, font=normal_font_style, width=20).grid(row=row_index, column=1, sticky='w')

    # 空行
    row_index += 1
    Label(main_frame, text="", font=blank_font_style).grid(row=row_index)
    row_index += 1
    Label(main_frame, text="", font=blank_font_style).grid(row=row_index)

    # buttons
    # 標準功能
    row_index += 1
    Button(main_frame, text="1. 已登記出席統計表」生成「計算完成統計表」\n"
                            "並「輸入資料庫」（標準流程）", font=normal_font_style,
           bg='skyblue', width=40, height=2, command=lambda: function_1(row_index)).grid(row=row_index, column=0, sticky='w')

    # 生成表功能
    Button(main_frame, text="2. 「已登記出席統計表」生成「計算完成統計表」\n（+ 黑名單、CARDO點數、報名方式等)",
           font=normal_font_style,
           bg='skyblue', width=40, height=2, command=lambda: function_2()).grid(row=row_index, column=1, sticky='w')

    # 空行
    row_index += 1
    Label(main_frame, text="", font=blank_font_style).grid(row=row_index)

    # 表輸入功能
    row_index += 1
    Button(main_frame, text="3. 「計算完成統計表」「輸入資料庫」", font=normal_font_style,
           bg='skyblue', width=40, height=2, command=lambda: function_3()).grid(row=row_index, column=0, sticky='w')

    # 空行
    row_index += 1
    Label(main_frame, text="", font=blank_font_style).grid(row=row_index)
    row_index += 1
    Label(main_frame, text="", font=blank_font_style).grid(row=row_index)


    # activate the app
    win.mainloop()
