from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

import os

from test import run_with_ngrok		#TODO: Remove testing code
import test

app = Flask(__name__)

run_with_ngrok(app)  				#TODO: Remove more testing code

CORS(app)                          	# CORS hates APIs being used like they normally are
app.url_map.strict_slashes = False 	# Fixes "/new/" vs "/new" error


@app.route('/<id>', methods = ['GET'])
def get_data(id):
	return jsonify(test.get(id))


@app.route('/new', methods = ['POST'])
def push_data():
    	key = test.add(request.get_json())
    	return jsonify({'key': key})


@app.route('/')
def index():
	return "Hello, World!"


@app.route('/favicon.ico')
def favicon():
    	return send_from_directory(os.path.join(app.root_path, 'static'),
                'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    	app.run()