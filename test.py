# -*- coding:utf-8 -*- 
'''
Created on 2016年1月20日

@author: chendq
'''
import web

urls = ('/upload', 'Upload')

render = web.template.render('templates/')

def copyFile():
    print 'copy file ok'
    return 

class Upload:
    def GET(self):
        return render.upload()

    def POST(self):
        x = web.input(myfile={})
        filedir = './files' # change this to the directory you want to store the file in.
        if 'myfile' in x: # to check if the file-object is created
            filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
            fout = open(filedir +'/'+ filename,'w') # creates the file where the uploaded file should be stored
            fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.
            copyFile()
        raise web.seeother('/upload')


if __name__ == "__main__":
    
    app = web.application(urls, globals()) 
    app.run()