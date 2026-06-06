from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<center><h1>Hola Mundo con Flask</h1></center>'

app.run(debug=True)