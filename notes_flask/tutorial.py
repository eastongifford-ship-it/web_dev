from flask import Flask, render_template, request, redirect, url_for 


app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        return redirect(url_for('user', name=request.form['name']))
    return render_template("index.html")
@app.route("/contact")
def contact():
    return "<p> Do not contact me DUMB DUMB! </p>"

@app.route("/<name>")
def user(name):
    return f"<h1> Hello, {name}! </h1>"

if __name__ == '__main__':
    app.run(debug=True)