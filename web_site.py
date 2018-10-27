from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Привет, мир! Кажется это мой первый сайт на Python"

app.run(port=8000)
