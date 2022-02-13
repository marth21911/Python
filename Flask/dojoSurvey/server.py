from flask import Flask, render_template, request, redirect, session



app = Flask(__name__)
app.secret_key = 'you didnt say the magic word'

@app.route ('/')
def index():
    return render_template( 'index.html')

@app.route('/results', methods=['POST'])
def dojo_survey():
    print("Got Post Info")
    print(request.form)
    session['name'] = request.form['name']
    session ['location'] = request.form['location']
    session ['language'] = request.form['language']
    session ['comments'] = request.form['comments']
    return redirect("/results")
@app.route("/results")
def results():
    print("Showing the survey Info From the Form")
    print(request.form)
    return render_template("results.html", name = session['name'], location = session['location'], option = session['language'], comments = session['comments'])



if __name__=="__main__":
    app.run(debug=True)