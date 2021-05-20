import os
import shutil
import time

path = input('Enter file name: ')
days = int(input("Enter the number of days you want to keep file: "))
seconds = time.time() - (days * 24 * 60 * 60)
exist = os.path.exists(path)

if(exist == True):
    os.walk(path)
    os.path.join(path)
    ctime = os.stat(path).st_ctime
    if(ctime > seconds):
        if(exist):
            os.remove(path)
        else:
            shutil.rmtree()
    else:
        print('Not found')
