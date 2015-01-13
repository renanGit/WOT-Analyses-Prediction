from subprocess import call
import os, shutil, datetime, wotbr2j as wot


def getFileList():
    path = os.getenv('APPDATA')
    cat = '\\Wargaming.net\\WorldOfTanks\\battle_results'
    current_dir = os.path.dirname(os.path.abspath(__file__))

    try:
        os.mkdir(current_dir + '\\json')
    except OSError as e:
        print e

    if os.path.isdir(path + cat):
        list = os.listdir(path + cat)
        cat += '\\' + list[0]
        battles = os.listdir(path + cat)
        for b in battles:
            print b
            callScript(path + cat + b)
            os.rename(path + cat + b[:-4], current_dir + '\\json\\' + datetime.datetime.now())

    # os.rename(src, dist)
    # os.stat(filename).st_mtime    # check if the dir was modified / returns time modified

def callScript(file_path):
    try:
        return_code = call(['python', 'wotbr2j.py', file_path], shell=False)
        if return_code < 0:
            print "Child was terminated by signal", -return_code
        else:
            print "Child returned", return_code
    except OSError as e:
        print "Execution failed:", e

getFileList()