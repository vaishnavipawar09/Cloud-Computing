from flask import Flask, send_file, make_response
import os
import hashlib
import random
import string
import sys

app = Flask(__name__)

@app.route('/')
def send_Randomfile():
    pathOfFile = '/serverdata/GeneratedFile.txt'
    checksum = create_Randomfile(pathOfFile)
    return send_fileAsResponse(pathOfFile, 'GeneratedFile.txt', checksum)

def create_Randomfile(pathOfFile):
    #Generate a file with random content and calculate its SHA-256 checksum.
    chars = string.ascii_letters + string.digits
    contentOfFile = ''.join(random.choice(chars) for _ in range(1024)) 
    with open(pathOfFile, 'w') as file:
        file.write(contentOfFile)

    return calChecksum(contentOfFile)

def calChecksum(data):
    #Calculate and return the SHA-256 checksum of the provided data.
    hasher256 = hashlib.sha256(data.encode('utf-8'))
    return hasher256.hexdigest()

def send_fileAsResponse(pathOfFile, Filename, checksum):
    #Send the file with a checksum header.
    response = make_response(send_file(pathOfFile, as_attachment=True, download_name='GeneratedFile.txt', mimetype='application/octet-stream'))
    response.headers['Checksum'] = checksum
    return response

if __name__ == '__main__':
    Serverport = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    app.run(host='0.0.0.0', port=Serverport)
