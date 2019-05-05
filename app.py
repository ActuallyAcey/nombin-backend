from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

import os

from test import run_with_ngrok		#TODO: Remove testing
import test

app = Flask(__name__)
run_with_ngrok(app)                # TODO: Remove Testing
CORS(app)                          # CORS hates APIs being used like they normally are
app.url_map.strict_slashes = False # Fixes "/new/" vs "/new" error

@app.route('/favicon.ico')
def favicon():
    	return send_from_directory(os.path.join(app.root_path, 'static'),
                'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
	return "Hello, World!"


@app.route('/<id>', methods = ['GET'])
def get_data(id):
	return jsonify(test.get(id))
	# TODO: Get from Database

@app.route('/new', methods = ['POST'])
def push_data():
    	key = test.add(request.get_json())
    	return jsonify({'key': key})


if __name__ == '__main__':
    	app.run()