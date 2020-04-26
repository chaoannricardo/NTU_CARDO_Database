from tkinter import *


def main_view():
    # construct a window
    win = Tk()
    win.title("NTU CARDO 資料庫管理系統")
    win.geometry("800x400+200+200")

    # create a frame
    main_frame = Frame(win)
    main_frame.pack(side=TOP, fill=X, padx=5)

    # create a text label
    main_text = "----------------------------------------------------------------------------------\n" + \
                "國立臺灣大學管理學院生涯發展中心（CARDO）資料處理及資料庫管理程式】\n" + \
                "# 歡迎使用本資料庫系統" + \
                "# 請輸入使用者帳號，或輸入'exit'離開本程式： \n 或輸入'admin'進入管理員介面（非管理員請勿使用，以免程式損壞）"

    main_text_label = Label(text=main_text)
    main_text_label.pack()

    # create buttons
    # button data processing
    btn_data_process = Button(text="活動\n建檔")
    btn_data_process.config(bg='skyblue', width=10, height=2)
    btn_data_process.pack()
    # button

    win.mainloop()


if __name__ == '__main__':
    main_view()