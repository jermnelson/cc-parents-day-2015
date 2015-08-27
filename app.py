__author__ = "Jeremy Nelson"

from flask import Flask, abort, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=21510, debug=True)
