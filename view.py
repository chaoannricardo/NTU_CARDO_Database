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


def log_in(account, password):
    try:
        config = get_config(account, password)
        # 身分驗證
        print('# 登入中....')
        conn = database_management.pymysql_connect(**config)
        print("# 登入成功，歡迎回來", account)
        t_sleep(1)
    except:
        print("# 您輸入的帳號或密碼錯誤，請再輸入一次。")
        print()
        print()
    return config


if __name__ == '__main__':
    # construct a window
    win = Tk()
    font_style = tkFont.Font(family="微軟正黑體", size=14)
    win.title("NTU CARDO 資料庫管理系統")
    win.geometry("800x500+100+100")

    # create a frame
    main_frame = Frame(win)
    main_frame.pack(side=TOP, fill=X, padx=5)

    # create a text label
    main_text = "----------------------------------------------------------------------------------\n" + \
                "【國立臺灣大學管理學院生涯發展中心（CARDO）資料處理及資料庫管理程式】\n"
    main_text_label = Label(text=main_text, font=font_style)
    main_text_label.pack()

    # licence label
    license_font_style = tkFont.Font(family="微軟正黑體", size=8)
    license_text = get_license()
    license_label = Label(text=license_text, font=license_font_style)
    license_label.pack()

    # create log in column
    account_label = Label(text="請輸入帳號：", font=font_style)
    account_label.pack()
    account_entry = Entry(font=font_style)
    account_entry.pack()

    br_label = Label(text="   ")
    br_label.pack()

    password_label = Label(text="請輸入密碼：", font=font_style)
    password_label.pack()
    password_entry = Entry(font=font_style)
    password_entry.pack()

    # create log in button
    br_label = Label(text="   ")
    br_label.pack()
    
    btn_login = Button(text="登入", font=font_style)
    btn_login.config(bg='skyblue', width=5, height=1)
    btn_login.pack()


    win.mainloop()
