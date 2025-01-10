import os
from bottle import route, request, static_file, run, redirect

@route('/')
def root():
    return static_file('index.html', root='.')

@route('/css/bulma.css')
def bulma():
    return static_file('bulma.css', root='css')

@route('/remote-control.png')
def favi():
    return static_file('remote-control.png', root='.')

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

    if os.path.exists(file_path):
        redirect('http://192.168.1.19:8080/open-pdf?file={file_path}'.format(file_path=file_path))
    else:
        upload.save(file_path)
        redirect('http://192.168.1.19:8080/open-pdf?file={file_path}'.format(file_path=file_path))

if __name__ == '__main__':
    run(host='0.0.0.0', port=9999)
