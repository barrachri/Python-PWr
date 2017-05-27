from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
@app.route('/hello/<string:name>/')
def hello(name=None):
    if name is None:
        return 'Hello there!'
    elif name == 'there':
        return 'General Kenobi!'
    else:
        return 'Hello {}!'.format(name)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Do some stuff to log a user using POST data.
        pass
    else:
        # Render login form allowing to log in.
        pass
    return 'Login'

if __name__ == '__main__':
    app.run()
