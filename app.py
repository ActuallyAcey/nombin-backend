from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_ngrok import run_with_ngrok 

import os

previous_post_key = 0

app = Flask(__name__)

run_with_ngrok(app)  				#TODO: Remove more testing code

# CONFIGURATIONS
                          	# CORS hates APIs being used like they normally are I guess?
app.url_map.strict_slashes = False 	# Fixes "/new/" vs "/new" error
app.config['MONGO_DBNAME'] = 'NomBinDB'
app.config['MONGO_URI'] = 'mongodb+srv://nom:nomnomnom@nombindb-i0qby.mongodb.net/test?retryWrites=true'

mongo = PyMongo(app)
CORS(app)

@app.route('/<id>', methods = ['GET'])
def get_data(id):

	check_id = int(id)

	noms = mongo.db.nom_list
	fetched_nom = noms.find_one({'key' : check_id})
	
	if "_id" in fetched_nom:
		print ("Detected id, stripping off.")
		del fetched_nom["_id"]

	return jsonify(fetched_nom)


@app.route('/new', methods = ['POST'])
def push_data():
	global previous_post_key
	data = request.get_json()

	new_nom = {	'key' : previous_post_key + 1,
				'title': data['title'],
        		'text': data['text'],
        		'tags': data['tags'],
        		'is_private': data['is_private']}

	noms = mongo.db.nom_list
	noms.insert(new_nom)
	previous_post_key += 1
	return jsonify({'key': previous_post_key - 1})


@app.route('/')
def index():
	return "Hello, World!"


@app.route('/favicon.ico')
def favicon():
    	return send_from_directory(os.path.join(app.root_path, 'static'),
                'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    	app.run()