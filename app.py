from flask import Flask, render_template
from borads_api import boards_bp
from cards_api import cards_bp
import requests



app = Flask(__name__)

app.register_blueprint(boards_bp, url_prefix='/api')
app.register_blueprint(cards_bp, url_prefix='/api')

@app.route("/")
def index():
    response = requests.get("http://127.0.0.1:5000/api/boards")


    return render_template("index.html", data=response.json())

if __name__ == "__main__":
    app()