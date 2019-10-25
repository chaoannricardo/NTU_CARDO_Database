# import packages needed
from pymysql import cursors
import data_processing as dp
import file_management as fm
import MySQL_management as sql
import Test as t


# Input information:
# "C:\Users\ricardo\Desktop\Data\0311_藍天百腦匯報名清單(登陸出席).csv"
file_path = input("【注意事項】\n請將從台大網站下載的'xls'檔案，以Excel開啟後，以'CSV (逗號分隔) (*.csv)'方式另存新檔)\n請輸入另存新檔後csv路徑(Shift+滑鼠右鍵 => 複製路徑): ")
year = input("請輸入年度(EX: 106, 107, 108....): ")
semester = input("請輸入年度(EX: 1, 2....): ")

# Process Starts
file_path, first_cat, second_cat = fm.get_file(file_path)
data = dp.data_processing(year, semester, file_path, first_cat, second_cat)

# Connect to MySQL database, and execute command
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'user',
    'password': 'password',
    'db': 'cardo',
    'charset': 'utf8mb4',
    'cursorclass': cursors.DictCursor,
}

table_name = sql.create(data, first_cat, second_cat, config)

#command = "CREATE TABLE Employee(id int, LastName varchar(32), FirstName varchar(32), DepartmentCode int)"


# Remove temporory file
fm.remove_temp()
