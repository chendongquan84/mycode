#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016年1月16日

@author: chendq
'''
import web
import myloger
import logging
import fileManger
androidFileDir = './static/apkFiles'
iosFileDir = './static/iosFiles'

class index:
    def GET(self):
        newAndroidName = 'android-test-2.4.1-8-0113151919.apk'
        newIosName = 'android-test-2.4.1-8-0113151919.apk'
        return render.index(newAndroidName,newIosName)
    def POST(self):
        data = web.data()
        logging.info(data)
        return 'success'
class android:
    def GET(self):
        androidVersion = fileManger.getFileList(androidFileDir)
        print androidVersion
        androidVersion.remove('new')
        if androidVersion:
            return render.android(androidVersion)
        else:
            return render.erro( '暂时还没有可下载android版本客户断')
class ios:
    def GET(self):
        iosVersion = fileManger.getFileList(iosFileDir)
        iosVersion.remove('new')
        if iosVersion:
            return render.ios(androidVersion)
        else:
            return render.erro( '暂时还没可下载ios版本客户端')
class androidVer:
    def GET(self,version):
        dir = '/'.join([androidFileDir,version])
        files = fileManger.getFileList(dir)
        if files:
            return render.fileDownList('/'.join([ '../..', androidFileDir ,version]),files)
        else:
            return render.erro('暂时还没有该版本客户端可下载')
class iosVer:
    def GET(self,version):
        dir = '/'.join([iosFileDir,version])
        files = fileManger.getFileList(dir)
        if files:
            return render.fileDownList('/'.join([ '../..', iosFileDir ,version]),files)
        else:
            return render.erro('暂时还没有该版本客户端可下载')
    
class test:
    def GET(self,test):
        return test

if __name__ == '__main__':
    
    urls = ("/", "index",
            "/android$","android",
            "/ios$","ios",
            "/android/ver/(.*\d)","androidVer",
            "/test/(.*)",'test')
    
    render = web.template.render('templates/')
    app = web.application(urls, globals())
    app.run()
    