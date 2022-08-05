import os
import re
import time
import os.path
from typing import List
from striprtf.striprtf import rtf_to_text
from pathlib import Path

#filemaskKS = "Выписка из казначейского счета"
#filemaskReestr = '0531465'
#filemaskBudget = '0531775'
#filemaskPBS = '0531759'
#fileADB = '0531761'
#prilfileBudget = '0531784'
#prilfilePBS = "0531778"
#prilADB = '0531779'
dir = os.getcwd()
filemaskAll = '0531465|0531775|0531759|0531761|0531784|0531779|0531778|Выписка из казначейского счета'
print('Введите дату отчётов')
timestr = input()
print('Введите дату реестров')
timeReestr = input()
#timeReestr = time.strftime("%d%m ")
def searchTextInFile(files: str) -> List[str]:
    result = []
    with open(files) as infile:
        content = infile.read()
        text = rtf_to_text(content)
        result = re.findall(filemaskAll, text)
    return result

def renameFile(result: List[str]) -> None:
    fileSpisok = filemaskAll.split('|')
    for number_file, name in enumerate(result):
        if name in fileSpisok:
            if name == '0531465':
                oldName = files.name

                newName = 'реестр поступлений'
                os.rename(files, str(timeReestr) + ' ' + newName + ' ' + oldName)
                print("REESTR")
            elif name == '0531775':
                oldName = files.name
                newName = 'выписка из бюджета'
                os.rename(files, str(timestr) + ' ' + newName + ' ' + oldName)
                print("BUDGET")
            elif name == '0531759':
                oldName = files.name
                newName = 'выписка из пбс'
                os.rename(files, str(timestr) + ' ' + newName + ' ' + oldName)
                print("PBS")
            elif name == '0531761':
                oldName = files.name
                newName = 'выписка из адб'
                os.rename(files, str(timestr) + ' ' + newName + ' ' + oldName)
                print("ADB")
            elif name == '0531784':
                oldName = files.name
                newName = 'приложение к бюджету'
                os.rename(files, str(timestr) + ' ' + newName + ' ' + oldName)
                print("PRILBUDGET")
            elif name == '0531779':
                oldName = files.name
                newName = 'приложение к АДБ'
                os.rename(files, str(timestr) + ' ' + newName + ' ' + oldName)
                print("PRILADB")
            elif name == '0531778':
                oldName = files.name
                newName = 'приложение к пбс'
                os.rename(files, str(timestr) + ' ' + newName + ' ' + oldName)
                print("PRILPBS")
            elif name == 'Выписка из казначейского счета':
                oldName = files.name
                newName = 'выписка кс'
                os.rename(files, str(timestr) + ' ' + newName + ' ' + oldName)
                print("KS")

for files in Path(dir).glob('*.RTF'):
    if not 'print' == files.name[:5]:
        continue
    result = searchTextInFile(files)
    renameFile(result)
input('Нажмите Enter')