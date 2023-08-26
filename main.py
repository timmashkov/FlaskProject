from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'''
    <!DOCTYPE html>
    <html>
        <head>
            <title> Home page </title>
            <meta charset='utf-8'>
        </head>
        <body>
            <p align='center'> The welcome data for user </p>
        </body>
    </html>
    '''

@app.route('/<path:x>')
def info(x):
    return f'{x}'
