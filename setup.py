import sys
from cx_Freeze import setup, Executable

exe = Executable(
    script="Main.py",
    base=None,
    targetName="Main.exe"\
    )

setup(name = "NTU_CARDO_Database",
      version = "0.1",
      description = "My GUI App",
      executables = [Executable("Main.py")])