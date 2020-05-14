from flask import Flask, request, redirect, url_for, flash, jsonify
import json
import os
import tools.files
import tasks

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/img'

# IMP LOCs
imgLoc = './img'
fileType = '.png'

@app.route('/')
def home():
    return "Server is listening..."

# For media/files
@app.route('/upload', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        fileRec = request.files['image']
        #Extracted ID can be used to store in individual folders = imgLoc + "/" + ID + "/" + str(tools.files.imgName()) + fileType
        name = imgLoc + str(tools.files.imgName()) + fileType
        fileRec.save(name)
        #Insert ID as argument if data being received should be personalised
        tasks.schedule()
        return "File Saved"
    elif request.method == 'GET':
        print("No GET Method yet")

# For standard HTTP requests
@app.route('/bruh', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        '''
            if 'id' in request.args:
                id = request.args.get('id')
            else:
                return "Error: No Id field provided."
        '''
        prediction = tasks.schedule(id)
        return prediction

if __name__ == '__main__':
    app.run()