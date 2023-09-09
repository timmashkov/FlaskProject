from random import choice, shuffle, randrange, randint

from flask import Flask
from flask import render_template, url_for, redirect

from instance.model import db, User, Post, Comment

app = Flask(__name__)
# Создаем базу данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
#  app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql:///username:password@hostmane/db_name' для mysql
#  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2:///username:password@hostmane/db_name' для postgresql
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


#@app.cli.command('init-db')
@app.route('/init-db')
def init_db():
    db.create_all()
    return redirect(url_for('index'))

#@app.cli.command('add-john')
@app.route('/add-john')
def add_user():
    user = User(username='John', email='John@example.com')
    db.session.add(user)
    db.session.commit()
    return render_template('temp_unit.html')



#  if __name__ == '__main__':
   #app.run(debug=True)
