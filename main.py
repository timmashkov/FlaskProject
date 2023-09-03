from random import choice, shuffle, randrange, randint

from flask import Flask
from flask import render_template, url_for

from instance.model import db

app = Flask(__name__)
# Создаем базу данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
db.init_app(app)


@app.route('/')
def index():
    print(url_for('index'))
    words = ['Pretty', 'Beautiful', 'Gorgeous', 'Great']
    shuffle(words)
    return render_template('index.html', word=choice(words), title='Initial page')


@app.route('/greeting')
def greeting():
    numbers = [i for i in range(randrange(randint(1, 1000)))]
    string = f'Your lucky number today is {choice(numbers)}'
    menu = ['News', 'Events', 'Contacts']
    return render_template('greeting.html', phrase=string, menu=menu)


@app.route('/temp_unit/<title>')
def temp_unit(title):
    return render_template('temp_unit.html', word=title)


if __name__ == '__main__':
    app.run(debug=True)
