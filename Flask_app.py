from flask import Flask, render_template, request



app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Welcome to Flask-app "


if __name__ == '__main__':
    app.run(port=5000)
