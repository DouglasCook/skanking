import random
from pathlib import Path

from flask import Flask, render_template, session


app = Flask(__name__)
app.secret_key = 'someLongRandomStringInnit'
static_path = Path('static')

@app.route('/', methods=['GET'])
def get_next():
    if not session.get('to_do'):
        print('REGENERATING TODO LIST')
        to_do = list(db.keys())
        random.shuffle(to_do)
        session['to_do'] = to_do

    # session doesn't update if mutated in place so can't use pop
    item = db[session['to_do'][0]]
    session['to_do'] = session['to_do'][1:]
    print(f"REMAINING {session['to_do']}")

    return render_template('page.html', image_path=static_path/item['file'])


db = {
    1: {'file': 'skanking.jpg', 'class': 'skanking'},
    2: {'file': 'bang_the_drum.jpg', 'class': 'wanking'},
    3: {'file': 'Dug-up.jpg', 'class': 'skanking'},
    4: {'file': 'snek.jpg', 'class': 'wanking'},
}
