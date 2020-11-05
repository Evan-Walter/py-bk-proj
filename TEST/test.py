import sys
import os
import shutil
import datetime
from datetime import date

# Variables
today = str(date.today())
src1test = 'C:/Users/evan/Dropbox/copy1'
dst1test = f'C:/Users/evan/Desktop/{today}'

if __name__ == '__main__':
    shutil.copytree(src1test, dst1test)
