from flask import Flask, request, flash, redirect, render_template, send_file, jsonify

import os
import datetime

from .modules.runner import Runner
   
runner = Runner()
#ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'doc', 'docx'}
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# ------------------------------------- RUN APP -------------------------------------------------
app = Flask(__name__)
app.config['PATH_TO_ZIP'] = None
app.config['SECRET_KEY'] = '12345'

@app.route('/', methods=['GET'])
def upload_file():
    return render_template('initial.html')

@app.route('/', methods=['POST'])
def main_page():
    #we shell use abs path ton relative! it break lauching script from other directory
    WORK_DIR = 'data/result_{}'.format(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    os.makedirs(WORK_DIR)
    app.config['WORK_DIR'] = WORK_DIR
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return  redirect(url_for('main_page'))
    if file:
        if allowed_file(file.filename):
            # если все ок, то сохраняем файл по директории UPLOAD_FOLDER
            filename = file.filename
            file_path = os.path.join(WORK_DIR, filename)
            file.save(file_path)
            # backend
            output_dir = os.path.join(WORK_DIR, os.path.basename(file_path).split('.')[0])
            os.mkdir(output_dir)
            results_path, path_to_zip = runner.process(file_path, output_dir, blur=True)
            app.config['PATH_TO_ZIP'] = path_to_zip
            return redirect('/processed/')
        else:
            flash('This file is not allowed')
            return  redirect(url_for('main_page'))
    return redirect(request.url)

@app.route('/wait/', methods=['GET'])
def upload_file_wait():
    return render_template('wait.html')
    
@app.route('/processed/', methods=['POST'])
def upload_file_post():
    try:
        return send_file(app.config['PATH_TO_ZIP'])
    except Exception as e:
        return str(e)
    
@app.route('/processed/', methods=['GET'])
def upload_file_get():
    return render_template('processed.html')

@app.route("/back/", methods=['POST'])
def move_back():
    for root, dirs, files in os.walk(app.config['WORK_DIR'], topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    if os.path.isdir.exists(app.config['WORK_DIR']):
        os.rmdir(app.config['WORK_DIR'])
    return  redirect(url_for('main_page'))


if __name__=='__main__': 
    #app.run(host='0.0.0.0', port='9889', debug=True)
    app.run(port="5000")
