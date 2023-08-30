from flask import Flask
from flask import render_template, url_for
from random import choice, shuffle, randrange, randint


app = Flask(__name__)

@app.route('/')
def index():
    words = ['Pretty', 'Beautiful', 'Gorgeous', 'Great']
    shuffle(words)
    return render_template('index.html', word=choice(words), title='Initial page')


@app.route('/greeting')
def greeting():
    numbers = [i for i in range(randrange(randint(1, 1000)))]
    string = f'Your lucky number today is {choice(numbers)}'
    menu = ['News', 'Events', 'Contacts']
    return render_template('greeting.html', phrase=string, menu=menu)

@app.route('/test_url_for/<int:x>')
def test_url(x):
    resp = f'The val x is {x}<br>'
    resp += f'Function url_for {url_for("test_url", x=x, data="new_data", sign="?")}'
    return resp


if __name__ == '__main__':
    app.run(debug=True)
