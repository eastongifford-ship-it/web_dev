from flask import Flask, render_template, request, redirect, url_for 


app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        return redirect(url_for('user', name=request.form['name']))
    return render_template("index.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/<name>")
def user(name):
    return f"<h1> Hello there you are not, {name}! You are now a banana! 🍌</h1>"

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)