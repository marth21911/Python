from flask import Flask, render_template
app = Flask(__name__)
@app.route('/<x>/<y>')
def index(x,y):
    print( "X squares =" + x)
    print( "y squares =" + y)
    return render_template("index.html", x=int(x), y=int(y))
if __name__=="__main__":
    app.run(debug=True)

