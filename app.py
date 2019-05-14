from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from flask_pymongo import PyMongo
from os import path

import server_secrets 

from flask_ngrok import run_with_ngrok

app = Flask(__name__)

run_with_ngrok(app)  				#TODO: Remove when deploying; used for exposing localhost as a temporary URL

# CONFIGURATIONS
                          	
app.url_map.strict_slashes = False 	# Fixes "/new/" vs "/new" error
app.config['MONGO_DBNAME'] = server_secrets.mongo_db_name
app.config['MONGO_URI'] = server_secrets.mongo_uri

mongo = PyMongo(app)
CORS(app)							# CORS hates APIs being used like they normally are I guess?

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

	data = request.get_json()

	new_nom = {
				'title': data['title'],
        		'text': data['text'],
        		'tags': data['tags'],
        		'is_private': data['is_private']}

	noms = mongo.db.nom_list
	key = noms.insert_one(new_nom).inserted_id

	return jsonify({'key': key})


@app.route('/')
def landing_page():
	return "Hello, World!" 


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon') 


if __name__ == '__main__':
    	app.run()