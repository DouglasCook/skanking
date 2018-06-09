import random
from pathlib import Path

from flask import Flask, render_template, session, request


app = Flask(__name__)
app.secret_key = 'someLongRandomStringInnit'
static_path = Path('static')


@app.route('/', methods=['GET'])
def get_next():
    if not session.get('to_do'):
        to_do = list(db.keys())
        random.shuffle(to_do)
        session['to_do'] = to_do

    session['current'] = session['to_do'].pop()

    return render_template(
        'page.html',
        image_path=static_path / db[session['current']]['file'],
    )


@app.route('/guess', methods=['POST'])
def guess():
    result = 'INCORRECT'
    if request.form.get('guess') == db[session['current']]['class']:
        result = 'CORRECT!'

    return render_template(
        'page.html',
        image_path=static_path / db[session['current']]['file'],
        result=result,
    )


db = {
    1: {'file': 'skanking.jpg', 'class': 'skanking'},
    2: {'file': 'bang_the_drum.jpg', 'class': 'wanking'},
    3: {'file': 'Dug-up.jpg', 'class': 'skanking'},
    4: {'file': 'snek.jpg', 'class': 'wanking'},
}
