from pymysql import cursors
from tkinter import *
from time import sleep as t_sleep
import database_management
import tkinter.font as tkFont


def get_license():
    text = "----------------------------------------------------------------------------------\n" + \
           "程式開發者：趙上涵；Ricardo S. Chao\n" + \
           "E-mail: richiechao95@gmail.com\n" + \
           "Linkedin: https://www.linkedin.com/in/chaoannricardo/\n" + \
           "本程式 Source Code 網址：https://github.com/chaoannricardo/NTU_CARDO_Database\n" + \
           "Version: 2.0; Last Modified Date: 2020/04/26\n" + \
           "程式導覽手冊：https://github.com/chaoannricardo/NTU_CARDO_Database/blob/master/GUIDE.md\n" + \
           "----------------------------------------------------------------------------------"
    return text


def get_config(account, password):
    config = {
        # 'host': '127.0.0.1',
        'host': '220.133.208.39',
        # 'host': '10.181.2.122',
        'port': 3306,
        'user': account,
        'password': password,
        'db': 'cardo',
        'charset': 'utf8mb4',
        'cursorclass': cursors.DictCursor,
    }
    return config


def log_in(account_entry, password_entry):
    try:
        account = account_entry.get()
        password = password_entry.get()
        config = get_config(account, password)
        conn = database_management.pymysql_connect(**config)
        second_phase()
    except:
        incorrect_font_style = tkFont.Font(family="微軟正黑體", size=8, weight=tkFont.BOLD)
        Label(main_frame, text="輸入帳號密碼不正確，請再輸入一次",
              font=incorrect_font_style, fg='red').pack()


def data_processing_menu():
    # clear the screen
    for widget in main_frame.winfo_children():
        widget.destroy()

    # construct menu
    menu_font_style = tkFont.Font(family="微軟正黑體", size=24)
    Label(main_frame, text="\n【資料建檔選單】",
          font=menu_font_style).pack()
    Label(main_frame, text="   ").pack()

    # construct function list
    




    pass


def blacklist_control_menu():
    pass


def second_phase():
    # clear the screen
    for widget in main_frame.winfo_children():
        widget.destroy()

    menu_font_style = tkFont.Font(family="微軟正黑體", size=24)
    Label(main_frame, text="\n登入成功\n請選擇所欲使用的功能",
          font=menu_font_style).pack()

    font_style = tkFont.Font(family="微軟正黑體", size=14)
    # create button for csv importing
    Label(main_frame, text="   ").pack()
    Button(main_frame, text="資料建檔", font=font_style, bg='skyblue', width=30, height=1,
           command=lambda: data_processing_menu()).pack()

    Label(main_frame, text="   ").pack()
    Button(main_frame, text="黑名單管理\n對不起上涵還沒有時間完成", font=font_style, bg='skyblue', width=30, height=2,
           command=lambda: blacklist_control_menu()).pack()


def first_phase():
    # create a text label
    main_text = "\n【國立臺灣大學管理學院生涯發展中心（CARDO）資料處理及資料庫管理程式】"
    Label(main_frame, text=main_text, font=font_style).pack()

    # licence label
    license_font_style = tkFont.Font(family="微軟正黑體", size=8)
    license_text = get_license()
    Label(main_frame, text=license_text, font=license_font_style).pack()

    # create log in column
    Label(main_frame, text="請輸入帳號：", font=font_style).pack()
    account_entry = Entry(main_frame, font=font_style)
    account_entry.pack()

    Label(main_frame, text="   ").pack()

    Label(main_frame, text="請輸入密碼：", font=font_style).pack()
    password_entry = Entry(main_frame, font=font_style)
    password_entry.pack()

    # create log in button
    Label(main_frame, text="   ").pack()
    Button(main_frame, text="登入", font=font_style, bg='skyblue', width=5, height=1,
           command=lambda: log_in(account_entry, password_entry)).pack()


if __name__ == '__main__':
    # construct window and main frame
    global win, main_frame, authenticate, conn
    win = Tk()
    font_style = tkFont.Font(family="微軟正黑體", size=14)
    win.title("NTU CARDO 資料庫管理系統")
    win.geometry("800x500+100+100")
    main_frame = Frame(win)
    main_frame.pack(side=TOP, fill=X, padx=5)

    # first phase
    first_phase()

    win.mainloop()
