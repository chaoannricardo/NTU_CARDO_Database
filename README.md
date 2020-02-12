# NTU_CARDO_Database

###  **Version**: 1.1

The program aims to tackle daily tasks , such as data-processing and database-managing, of CARDO (Career Development Office of College of Management) of National Taiwan University. 

* [Required Environment](#required-environment)
* [Build-up](#build-up)
* [Code Description](#code-description)
* [Functions](#functions)

<br>

# Required Environment
* **Python 3.7**
* **Numpy**
* **Pandas**
* **PyMySQL**
* **PyInstaller** (Needed only if you would like to build up the code into an exe file.)

<br>

# Build-up

**Before building up the program, make sure that you have**:

1. Installed MySQL database server inside your operating system (testing environment is Ubuntu 18.04)
2. Granted remote access and implement ODBC feature of the database.
3. Create a account inside the database and have granted the account with sufficient privileges.
4. Create a database with the correct charset. (database of the testing environment is using "utf8mb4_general_ci" as the charset of the database.)

```sql
-- Create a database with utf8 charset
CREATE DATABASE cardo CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

<br>

**There are two ways to build up the program:**

1. Pack up the code into a **windows .exe file** with **PyInstaller** command inside the directory. To pack up the code in this way, simply type:

```shell
pyinstaller -F ./__init__.py
```

​	If you do not have PyInstaller inside your environment, you could install it by following commands:

```shell
pip install pyinstaller
# or following command if above one does not work.
pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz
```

2. Execute the program by the **execute.sh** script, if you feel like to execute the program in this method, you must ensure the packages required is correctly installed inside your Anaconda or system environment, or the program may not act correctly. (See [Required Environment](#required-environment]))

<br>

**Running the program the first time:**

1. Make sure that above requirements have been set up correctly.
2. Remember to initiate **"主資料表"** to establish a main table for later insert usage.

<br>

**To update the program:**

  Simply execute **update.sh** script, the script would automatically update the repository to the latest git version. (by force)

<br>

# Code Description

* database_management.py:
* data_processing.py:
* file_management.py:
* __init__.py:
* execute.sh:

