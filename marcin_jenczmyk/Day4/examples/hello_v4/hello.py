from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/hello/<string:name>')
def hello(name=None):
    from flask import render_template

    if name == 'there':
        greetings = 'General Kenobi!'
    else:
        greetings = 'Hello {}!'.format(name or 'there')

    return render_template(
        'index.html',
        greetings=greetings
    )

if __name__ == "__main__":
    app.run()
