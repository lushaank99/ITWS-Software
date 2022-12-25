from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/comp/')
def comp():
    return render_template("comp.html")

"""Companies List"""
@app.route('/apple/')
def apple():
    return render_template("apple.html")

@app.route('/microsoft/')
def microsoft():
    return render_template("microsoft.html")

@app.route('/google/')
def google():
    return render_template("google.html")

@app.route('/amazon/')
def amazon():
    return render_template("amazon.html")

@app.route('/facebook/')
def facebook():
    return render_template("facebook.html")

@app.route('/bhathaway/')
def bhathaway():
    return render_template("bhathaway.html")

@app.route('/tesla/')
def tesla():
    return render_template("tesla.html")

@app.route('/disney/')
def disney():
    return render_template("disney.html")

if __name__=="__main__":
    app.run(debug=True)
