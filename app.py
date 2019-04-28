from flask import Flask, jsonify
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

testdata = {
        'paste': 'Magna quis ad esse pariatur sunt veniam cupidatat. Ullamco exercitation ad incididunt labore sint mollit ullamco sunt sint do reprehenderit. Cupidatat ea deserunt anim et commodo in adipisicing laborum laborum duis irure aliqua sit. Lorem amet laboris proident velit Lorem magna officia non excepteur dolor. Consectetur adipisicing deserunt sint laborum sunt nulla ullamco non duis.', 
        'password': 'totally secure password',
        'numbers': 20175719283
        }

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/test')
def test():
    return jsonify(testdata)

if __name__ == '__main__':
    app.run(