from flask import Flask, render_template, request, redirect, session



app = Flask(__name__)
app.secret_key = 'you didnt say the magic word'


@app.route('/')

def counter():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1
    return render_template('index.html')

@app.route('/2')
def plus_two():
    if "count" in session:
        session["count"] += 2
    return render_template('index.html')



@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)