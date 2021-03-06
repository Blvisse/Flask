import datetime

from flask import Flask, render_template

# Trying to recreate isichristmas.com

app = Flask(__name__)


@app.route('/')
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template('isitnewyears.html', new_year=new_year)


@app.route('/wishes')
def wishes():
    wish = ['Golf Gti', 'McLaren720s', 'Travel', ' Money ', 'Happiness']
    return render_template('wishez.html', wish=wish)


if __name__ == '__main__':
    app.run()
