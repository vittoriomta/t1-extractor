from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
import os
from script import extract
from sortexcel import sortdocs
from merge import merge
from master import masterall
from flask import Flask
app = Flask(__name__)



app.secret_key = 'mysecretkey'

app.config["UPLOAD_DIR"] = "folder/upload"
app.config["INPUT_MASTER"] = "folder/input"
app.config["OUTPUT_MASTER"] = "folder/output"

@app.route('/', methods = ["GET", "POST"])
def upload_files():
    if request.method == 'POST':
        if request.form.get('delete-files') == 'true':
            for directory in ['folder/input', 'folder/upload', 'folder/output']:
                if os.listdir(directory):
                    for file in os.listdir(directory):
                        os.remove(os.path.join(directory, file))
            return redirect(url_for('upload_files'))

        if 'form1' in request.form:
            files = os.listdir(app.config["UPLOAD_DIR"])
            for file in request.files.getlist('file1'):
                file.save(os.path.join(app.config['UPLOAD_DIR'], file.filename))
        elif 'form2' in request.form:
            files = os.listdir(app.config["INPUT_MASTER"])
            for file in request.files.getlist('file2'):
                file.save(os.path.join(app.config['INPUT_MASTER'], file.filename))

    return render_template('index.html')


@app.route("/extractor", methods = ["GET", "POST"])
def functions():
    if 'extract-input' in request.form: 
        if request.method == 'POST':
            extract(app.config["UPLOAD_DIR"])
            return redirect(url_for('download'))
    elif 'sort-input' in request.form: 
        if request.method == 'POST':
            sortdocs(app.config["INPUT_MASTER"],app.config["OUTPUT_MASTER"])
            return redirect(url_for('download'))
    elif 'merge-input' in request.form: 
        if request.method == 'POST':
            merge()
            return redirect(url_for('download')) 
    elif 'master-input' in request.form: 
        if request.method == 'POST':
            masterall()
            return redirect(url_for('download'))   
    return render_template('extractor.html')    
    
    

@app.route('/download')
def download():
        return render_template('download.html', files=os.listdir(app.config['OUTPUT_MASTER']))

@app.route('/download/<filename>')
def download_file(filename):
        return send_from_directory(app.config['OUTPUT_MASTER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
