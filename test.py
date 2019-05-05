from flask_ngrok import run_with_ngrok 
import requests

previous_post_key = 0

uploaded_noms = [
        {
        'key': 100,
        'title': 'First Title',
        'text': 'Magna quis ad esse pariatur sunt veniam cupidatat. Ullamco exercitation ad incididunt labore sint mollit ullamco sunt sint do reprehenderit. Cupidatat ea deserunt anim et commodo in adipisicing laborum laborum duis irure aliqua sit. Lorem amet laboris proident velit Lorem magna officia non excepteur dolor. Consectetur adipisicing deserunt sint laborum sunt nulla ullamco non duis.', 
        'tags': ['tag1', 'tag2', 'ugly bastard ( ͡° ͜ʖ ͡°)'],
        'is_private': False
        },

        {
        'key': 101,
        'title': 'Second Title',
        'text': 'Consequat commodo eu culpa sit cillum magna pariatur occaecat proident proident. Pariatur adipisicing non do velit labore. Adipisicing nostrud ipsum non ullamco sit consequat sunt deserunt dolore ex ad officia. Pariatur cupidatat est nulla quis nostrud irure amet laborum minim deserunt ad ullamco officia incididunt. Aliqua ullamco id eu ea consequat incididunt aute labore qui dolor qui.',
        'tags': ['tag3', 'tag4', 'STILL ugly bastard ( ͡° ͜ʖ ͡°)'],
        'is_private': True
        }
]

def add(data):
    global previous_post_key
    uploaded_noms.append({'key': previous_post_key + 1, 
                'title': data['title'],
                'text': data['text'],
                'tags': data['tags'],
                'is_private': data['is_private']
                })

    previous_post_key += 1
    return previous_post_key

def get(key):
 
        if (id == 'favicon.ico'):
        	{"message": "favicon"}

        check_id = int(key)
        for nom in uploaded_noms:
                if nom['key'] == check_id:
                	return nom
        
        return {"message": "No post found"}

	