from flask import Flask, render_template, redirect
app = Flask(__name__)
counter = 0

@app.route("/")
def homepage():
     return render_template('Radko clicker.html', count = counter)

@app.route("/click")
def clicking():
    global counter
    counter += 1
    return redirect("/")



app.run()
