#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年11月14日

@author: chendq
'''
import web
import os
import fileManger
import myloger
import logging
myloger.update_logging('./logs/callback.log')

host = 'http://182.254.213.25:8100'
apkDir = './static/apkFiles'
newApkDir = './static/apkFiles/newApk'
imgDir_ = './static/img'
backupApkDir = './static/apkFiles/backup'

render = web.template.render('templates/')
urls = ( '^/$','index','^/version(.+)','index1','^/backup$','backup')


class index:
    def GET(self):
        newApkName = fileManger.getApkName(newApkDir)
        newApkPath = newApkDir + '/' + newApkName
        newImgName = fileManger.getImgName(newApkName)
        imgPath = imgDir_ +'/' + newImgName
        fileManger.makeQrcode(host + '/static/apkFiles/newApk/' + newApkName ,imgPath)
        versionList = fileManger.getVersionList(apkDir)
        
        return render.index(versionList,newApkName,newApkPath,imgPath)
    def POST(self):
        data = web.data()
        logging.info(data)
        return 'success'
       
class index1:
    def GET(self,version):
        apkName = fileManger.getApkName('/'.join([apkDir,version]))
        apkPath = '/'.join([apkDir,version,apkName])
        androidVersion = version
        QRimgPath = '/'.join([imgDir_,fileManger.getImgName(apkName)])
        fileManger.makeQrcode('/'.join([host,'static/apkFiles',version,apkName]), QRimgPath)
        return render.version(androidVersion,apkPath,apkName,QRimgPath)

class backup:
    def GET(self):
        backupApkList = fileManger.getFileList(backupApkDir)
#        print backupApkList
        return render.backup(backupApkList,backupApkDir)
    
if __name__ == '__main__':
    test = index()
    test.GET()
    
    app = web.application(urls,globals())
    app.run()
