# Python:   version 2.7.13

#Author:    Curt Knutson

#Purpose:   Demonstrate knowledge of Python 2.7 to
#           Move files from src to dst folder if modified in last 24 hours

import shutil
import os
import time


def start():
    src = '/Users/curts/desktop/branchOffice'
    dst = '/Users/curts/desktop/homeOffice'
    moverecentfiles(src,dst)

def moverecentfiles(src,dst):
    timenow = time.time()
#   print(timenow)
    names = os.listdir(src)
#   print(names)
    for name in names:
        srcname = os.path.join(src,name)
#        print(srcname)
        dstname = os.path.join(dst,name)
#        print(dstname)
        modifiedTime = os.path.getmtime(srcname)
        elapsedTime=timenow-modifiedTime
        if elapsedTime < 86400:
            shutil.copy(srcname,dstname)
#        print(elapsedTime)

if __name__ == "__main__":
    start()
