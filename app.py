from flask import Flask, jsonify
from flask_ngrok import run_with_ngrok
from flask_cors import CORS

app = Flask(__name__)
run_with_ngrok(app)
CORS(app)


testdata1 = {
        'title': 'First Title',
        'text': 'Magna quis ad esse pariatur sunt veniam cupidatat. Ullamco exercitation ad incididunt labore sint mollit ullamco sunt sint do reprehenderit. Cupidatat ea deserunt anim et commodo in adipisicing laborum laborum duis irure aliqua sit. Lorem amet laboris proident velit Lorem magna officia non excepteur dolor. Consectetur adipisicing deserunt sint laborum sunt nulla ullamco non duis.', 
        'tags': ['tag1', 'tag2', 'ugly bastard ( ͡° ͜ʖ ͡°)'],
        'is_private': False
        }

testdata2 = {
        'title': 'Second Title',
        'text': 'Consequat commodo eu culpa sit cillum magna pariatur occaecat proident proident. Pariatur adipisicing non do velit labore. Adipisicing nostrud ipsum non ullamco sit consequat sunt deserunt dolore ex ad officia. Pariatur cupidatat est nulla quis nostrud irure amet laborum minim deserunt ad ullamco officia incididunt. Aliqua ullamco id eu ea consequat incididunt aute labore qui dolor qui.',
        'tags': ['tag3', 'tag4', 'STILL ugly bastard ( ͡° ͜ʖ ͡°)'],
        'is_private': True
        }

incoming_data = []

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/api/test/<id>', methods = ['GET'])
def test(id):

        if (id == 'set1'):
                return jsonify(testdata1)
        elif (id == 'set2'):
                return jsonify(testdata2)


@app.route('/api/test/', methods = ['POST'])
def push_data():
        pass
        
if __name__ == '__main__':
    app.run()