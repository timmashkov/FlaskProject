from flask import Flask
from flask import render_template
from random import choice, shuffle, randrange, randint


app = Flask(__name__)

@app.route('/')
def index():
    words = ['Pretty', 'Beautiful', 'Gorgeous', 'Great']
    shuffle(words)
    return render_template('index.html', word=choice(words))


@app.route('/greeting')
def greeting():
    numbers = [i for i in range(randrange(randint(1, 1000)))]
    string = f'Your lucky number today is {choice(numbers)}'
    return render_template('greeting.html', phrase=string)


if __name__ == '__main__':
    app.run(debug=True)
