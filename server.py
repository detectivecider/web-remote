import os
import requests
from bottle import route, request, static_file, run, redirect
import fileinput
import socket

ip = (([[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]
ip_js = "'http://" + ip + ":8080/'"

file = open('assets/js/script.js')
def findip():
    for line in file:
        if "http" in line:
            for old_ip in line.strip().split():
                if "http" in old_ip:
                    return old_ip
old_ip = findip()
for line in fileinput.input('assets/js/script.js', inplace = 1):
    print(line.replace(old_ip, ip_js).strip())

 #for item in files:
#    if "http" in item:
#        exp = findip()
#        print(str(item).replace(exp,ip), end="")
#    else:
#        print(str(item), end="")

#for line in fileinput.input(files, inplace = 1): 
#      print(line.replace("foo", "bar")),


@route('/')
def root():
    return static_file('index.html', root='.')

@route('/css/bulma.css')
def bulma():
    return static_file('bulma.css', root='assets/css')
@route('/css/sheet.css')
def sheet():
    return static_file('sheet.css', root='assets/css')

@route('/assets/remote-control.png')
def favi():
    return static_file('remote-control.png', root='assets')

@route('/js/script.js')
def favi():
    return static_file('script.js', root='assets/js')

@route('/upload', method='POST')
def do_upload():
    category = request.forms.get('category')
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.pdf'):
        return "File extension not allowed."

    save_path = "/tmp/{category}".format(category=category)
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    ip_path=('http://'+ip+':8080/open-pdf?file='+file_path)
    ip_front=('http://'+ip+':9999')
    if os.path.exists(file_path):
        requests.get(ip_path)
        redirect(ip_front)
    else:
        upload.save(file_path)
        requests.get(ip_path)

        redirect(ip_front)


if __name__ == '__main__':
    run(host='0.0.0.0', port=9999)
