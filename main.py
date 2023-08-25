from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'''<p1>Hello world</p1>
<p2>This is the initial writing</p2>'''

@app.route('/<path:x>')
def info(x):
    return f'{x}'
