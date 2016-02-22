#!/usr/bin/env python
# coding: utf-8

"""
    Image Resize API
    ~~~~~~
    이미지믈 입력받아 사이즈 변환하는 JSON 형태로 반한 하는 API

    /resize

"""

import os.path
import uuid
from flask import Flask, render_template, jsonify, request, send_from_directory

import imageresize

app = Flask(__name__)
UPLOAD_PATH = "upload"

@app.route('/')
def index():
	#return jsonify({'1':2})
	return render_template('index.html', error=None)

@app.route('/resize', methods = ['GET','POST'])
def resize():
	result = {}
	if request.method == 'POST' and 'file' in request.files:
		upload_file = request.files['file']
		if not upload_file:
			result['result'] = -100
			result['error']  = 'upload file error!!!'
			return jsonify(result)

		file_name = os.path.join(app.config['UPLOAD_PATH'], str(uuid.uuid4()).replace("-", ""))
		upload_file.save(file_name)
		thumbnail = []
		error = imageresize.resize(file_name, app.config['UPLOAD_PATH'], thumbnail)
		result['result'] = error[0]
		result['error']  = error[1]

		for item in thumbnail:
			item['uri'] = "/download/{}".format( item['filename'] )

		result['thumbnail'] = thumbnail
	else:
		result['result'] = -101
		result['error']  = 'upload file error!!!'

	return jsonify(result)

@app.route('/download/<path:filename>', methods = ['GET', 'POST'])
def download(filename):
	return send_from_directory(directory=app.config['UPLOAD_PATH'], filename=filename)

if __name__ == '__main__':
	app.config['UPLOAD_PATH'] = os.path.join(app.root_path, UPLOAD_PATH)
	app.run(debug=True)
