from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import time
#importing functions


#mentioning the upload folder 
UPLOAD_FOLDER = './data/input'

app = Flask(__name__)
#setting up the config for the app//upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/upload')
def upload():
   return render_template('upload.html')


@app.route('/uploader', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        files = request.files.getlist("file[]")

        for file in files:
            fn= secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], fn))
        
        
        return 'File uploaded successfully'


if __name__ == '__main__':
   app.run(debug = True)