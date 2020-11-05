# Evan Walter
# This program copies files from four AutoCAD-related folders to four Dropbox backup subfolders.
# For Cases 1 and 3, files that have been modified after a certain date are copied.
# For Cases 2 and 4, all files are copied.


import sys
import os
import shutil
import datetime
from datetime import date


# Variables
today = str(date.today())

# Test Variables
# src1test = 'C:/Users/evan/Dropbox/dpbx-docs/notes'
# dst1test = f'C:/Users/evan/Dropbox/paste1/{today}'

# Case 1, dwg
src1 = 'C:/Users/Public/Documents/Autodesk/Acade 2020/Libs/jic125'
dst1 = f'C:/Users/evan/Dropbox/dpbx-backups/acad/cust-syms-dwg/{today}'
# Case 2, png
src2 = 'C:/Users/evan/AppData/Roaming/Autodesk/AutoCAD Electrical 2020/R23.1/enu/Support/IMAGES'
dst2 = f'C:/Users/evan/Dropbox/dpbx-backups/acad/cust-syms-png/{today}'
# Case 3, tmp
src3 = 'C:/Users/evan/AppData/Local/Autodesk/AutoCAD Electrical 2020/R23.1/enu/Template'
dst3 = f'C:/Users/evan/Dropbox/dpbx-backups/acad/cust-templates/{today}'
# Case 4, plc
src4 = 'C:/Users/evan/Documents/Acade 2020/AeData/en-US/Plc'
dst4 = f'C:/Users/evan/Dropbox/dpbx-backups/acad/Plc/{today}'


# Mod date for ignore_by_date1/Case 1
def date1():
    return datetime.date(2019, 12, 1)


# Mod date for ignore_by_date3/Case 3
def date3():
    return datetime.date(2019, 10, 1)


def ignore_by_date1(src, contents=os.listdir('.')):
    os.chdir(src)
    return [name for name in os.listdir(src)
            if date.fromtimestamp(os.path.getmtime(name)) < date1()
            ]


def ignore_by_date3(src, contents=os.listdir('.')):
    os.chdir(src)
    return [name for name in os.listdir(src)
            if date.fromtimestamp(os.path.getmtime(name)) < date3()
            ]


if __name__ == '__main__':
    # Test Cases
    # shutil.copytree(src1test, dst1teset)
    # shutil.copytree(src1test, dst1test, ignore=ignore_by_date1)

    # Case 1
    shutil.copytree(src1, dst1, ignore=ignore_by_date1)
    # Case 2
    shutil.copytree(src2, dst2)
    # Case 3
    shutil.copytree(src3, dst3, ignore=ignore_by_date3)
    # Case 4
    shutil.copytree(src4, dst4)
