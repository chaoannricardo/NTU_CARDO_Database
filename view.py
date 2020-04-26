from pymysql import cursors
from tkinter import *
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
    global config
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


def destroy_frame(frame):
    frame.destroy()


def log_in(account_entry, password_entry):
    try:
        account = account_entry.get()
        password = password_entry.get()
        get_config(account, password)
        conn = database_management.pymysql_connect(**config)
    except:
        # clean up caution frame if there's anything inside
        if "caution_frame" in locals():
            destroy_frame(caution_frame)
        else:
            caution_frame = Frame(win)

        # delete config if log in process is not completed.
        if "config" in globals():
            del config


        incorrect_font_style = tkFont.Font(family="微軟正黑體", size=14, weight=tkFont.BOLD)
        incorrect_message_label = Label(caution_frame, text="您所輸入的帳號密碼不正確，請再輸入一次",
                                        font=incorrect_font_style, fg='red').pack()


if __name__ == '__main__':
    # construct a window
    global win
    win = Tk()
    font_style = tkFont.Font(family="微軟正黑體", size=14)
    win.title("NTU CARDO 資料庫管理系統")
    win.geometry("800x500+100+100")

    # create a frame
    main_frame = Frame(win)
    main_frame.pack(side=TOP, fill=X, padx=5)

    # create a text label
    main_text = "\n【國立臺灣大學管理學院生涯發展中心（CARDO）資料處理及資料庫管理程式】"
    main_text_label = Label(main_frame, text=main_text, font=font_style).pack()

    # licence label
    license_font_style = tkFont.Font(family="微軟正黑體", size=8)
    license_text = get_license()
    license_label = Label(main_frame, text=license_text, font=license_font_style).pack()

    # create log in column
    account_label = Label(main_frame, text="請輸入帳號：", font=font_style).pack()
    account_entry = Entry(main_frame, font=font_style).pack()

    br_label = Label(main_frame, text="   ").pack()

    password_label = Label(main_frame, text="請輸入密碼：", font=font_style).pack()
    password_entry = Entry(main_frame, font=font_style).pack()

    # create log in button
    br_label = Label(main_frame, text="   ").pack()

    btn_login = Button(main_frame, text="登入", font=font_style, bg='skyblue', width=5, height=1,
                       command=lambda: log_in(account_entry, password_entry)).pack()





    win.mainloop()
