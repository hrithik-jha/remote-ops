import requests
import os
    
URL = 'http://localhost:5000/upload'

def sendImage(i):
    image_filename = os.path.basename(i)
    multipart_form_data = {
        'image': (image_filename, open(i, 'rb')),
    }
    response = requests.post(URL, files=multipart_form_data)
    print(response)



# Create Loop to send stream
file = "./file.jpg"
sendImage("./file.jpg")