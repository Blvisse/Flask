from flask import Flask, render_template

app = Flask(__name__)


# The default route returns Hello world
@app.route('/')
def index():
    return 'Hello World'


@app.route('/david')
def david():
    return 'Hello,David'


@app.route('/Maria')
def Maria():
    return 'Hello Maria'


# This function allows the user to type any string as the route and returns the string name
@app.route('/<string:name>')
def hello(name):
    name = name.capitalize()  # capitalizes the first letter of the name
    return f'<p>Hello, {name}</p>'


@app.route('/template')
def rendered():
    return render_template('index.html')


@app.route('/headline')
def headL():
    headline = 'Hello This is the Headline'
    return render_template('index.html', headline=headline)


# runs our file

if __name__ == "__main__":
    app.run()
