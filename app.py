from flask import Flask
from flask import escape
app = Flask(__name__)

@app.route('/user/<name>')
# @app.route('/home')
def hello(name):
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif"><h1>Hello Totoro!</h1>  %s' %escape(name)