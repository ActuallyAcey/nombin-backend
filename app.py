from flask import Flask, jsonify, request
from test import run_with_ngrok
from flask_cors import CORS

app = Flask(__name__)
run_with_ngrok(app)                # TODO: Testing
CORS(app)                          # CORS hates APIs being used like they normally are
app.url_map.strict_slashes = False # Fixes "/new/" vs "/new" error

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/<id>', methods = ['GET'])
def test(id):
        return jsonify(test.get(id)) 


@app.route('/new', methods = ['POST'])
def push_data():
        data = request.get_json()
        key = test.add(data)

        return jsonify({'key': key})


if __name__ == '__main__':
    app.run()