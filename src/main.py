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

@app.route('/upload', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        fileRec = request.files['image']
        name = imgLoc + str(tools.files.imgName()) + fileType
        fileRec.save(name)
        #Insert ID as argument if data being received should be personalised
        tasks.schedule()
        return "File Saved"
    elif request.method == 'GET':
        print("No GET Method yet")

app.run()
