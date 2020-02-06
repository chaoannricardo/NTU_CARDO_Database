# NTU_CARDO_Database

###  **Version**: 0.0.0 **(Still under construction)**

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

**There are two ways to build up the program:**

1. Pack up the code into a **windows .exe file** with **PyInstaller** command inside the directory. To pack up the code in this way, simply type:

```shell
pyinstaller -F ./Main.py
```

​	If you do not have PyInstaller inside your environment, you could install it by following commands:

```shell
pip install pyinstaller
# or following command if above one does not work.
pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz
```

2. Execute the program by the **execute.sh** script, if you feel like to execute the program in this method, you must ensure the packages required is correctly installed inside your Anaconda or system environment, or the program may not act correctly. (See [Required Environment](#required-environment]))



<br>



**To update the program:**

  Simply execute **update.sh** script, the script would automatically update the repository to the latest git version. (by force)

<br>

# Code Description

* DatabaseManagement.py:
* DataProcessing.py:
* FileManagement.py:
* Main.py:
* start_the_program.sh:

<br>

# Functions



