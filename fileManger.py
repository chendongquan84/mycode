#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年11月14日

@author: chendq
'''

import os
#import qrcode
import time
import shutil 

def getFileList(fileDir):
    try:
        list = os.listdir(fileDir)
        list.reverse()
        return list
    except:
        return None

def getApkName(fileDir):
    try:
        return os.listdir(fileDir)[0]
    except:
        return 'nofind'

def getImgName(apkName):
    fileName = apkName.split('.')[0]
    return fileName + '.png'

def getNewApkName_backup(apkName,num=-5):
    # apkname='test-2.20-2.apk'
    temp = list(apkName)
    try:
        temp[num] = str(int(temp[num]) + 1)
    except:
        print'原文件命名规则可能错误'
    return''.join(temp)

def getNewApkName(apkType,version,oldApkName):
    apkType = apkType
    version = version
    try:
        number = str(int(list(oldApkName)[-16]) + 1)
        return '-'.join([apkType,version,number,time.strftime("%m%d%H%M%S", time.localtime())+'.apk'])
    except Exception, e:
        print e

def clearDir(path):
    names = os.listdir(path)
    for name in names:
        _path = '/'.join([path,name])
        if os.path.isfile(_path):
            try:
                os.remove(_path)
            except Exception, e:
                print e
        else:
            try:
                os.rmdir(_path)
            except Exception, e:
                print e
    return

def copyIos(dir,path):
    fileName = getFileList(dir)[0]
    print fileName
    if 'ipa' in fileName:
        shutil.copy2('/'.join([dir,fileName]), path)
        print 'copy %s to %s ok at %s' % (fileName,path,time.strftime("%y%m%d%H%M%S", time.localtime()))
    return
        

if __name__ == '__main__':
    copyIos('./files', './static/iosFiles/new/')



