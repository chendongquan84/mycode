#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年12月16日

@author: chendq
'''

import fileManger
import shutil 
#import time

version = '2.4.1'
workerDir = '/data2/test/myWebTest'
apkType = 'android-test'
#apkType = 'android-simulation'
#apkType = 'android-release'
jekinsApk = '/data2/jenkins_work/jobs/rrkd_android_client_2.1.6/workspace/app/build/outputs/apk/app-rrkd-release.apk'



# 清空new目录
newDir = '/'.join([workerDir,'static/apkFiles/newApk'])
oldName = fileManger.getApkName(newDir)
newApkName = fileManger.getNewApkName(apkType,version,oldName)
newApkPath = '/'.join([newDir,newApkName])
print newApkName
fileManger.clearDir(newDir)
# # 复制最新包到 temp
shutil.copy2(jekinsApk,newApkPath)
# # 清空version目录
versionDir = '/'.join([workerDir,'static/apkFiles',version])
print versionDir
fileManger.clearDir(versionDir)
# 复制新apk到对应版本文件夹中
shutil.copy2(newApkPath,versionDir)

# 复制新apk到backup
backupDir = '/'.join([workerDir,'static/apkFiles/backup'])
shutil.copy2(newApkPath,backupDir)

