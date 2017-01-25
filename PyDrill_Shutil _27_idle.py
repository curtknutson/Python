# Python:   version 2.7.13

#Author:    Curt Knutson

#Purpose:   Demonstrate knowledge of Python 2.7 to
#           Move files from src to dst folder

import shutil
import os


def start():
    src = '/Users/curts/desktop/Folder_A'
    dst = '/Users/curts/desktop/Folder_B'
    movefiles(src,dst)

def movefiles(src,dst):
    names = os.listdir(src)
#   print(names)
    for name in names:
        srcname = os.path.join(src,name)
#        print(srcname)
        dstname = os.path.join(dst,name)
        print(dstname)
        shutil.move(srcname,dstname)

if __name__ == "__main__":
    start()
