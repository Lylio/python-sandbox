from flask import Flask, render_temp

app = Flask(__name__)


#To view the app, run script1.py and open browser at http://127.0.0.1:5000/

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)

