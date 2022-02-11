
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)
"""
@app.route('/dojo') 
def dojo():
    return 'dojo!'
v 
@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name
@app.route('/repeat/<num>/<word>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'

def repeat(word, num):

    return (word * int(num))

"""

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
