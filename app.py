from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")

def sample():
    return render_template("index.html")
@app.route("/home")

def home():
    return render_template("stud.html")
@app.route("/contact")

def contacts():
    return render_template("about.html")
@app.route("/about")

def about():
    return "<h4>you are in abourt</h5>"
if(__name__=="__main__"):
    app.run(debug=True)