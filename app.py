from flask import Flask, render_template
from borads_api import boards_bp
from cards_api import cards_bp
import requests
from flask import Blueprint, jsonify, request, make_response
from data_manager import execute_select, execute_insert
import data_handler


app = Flask(__name__)

app.register_blueprint(boards_bp, url_prefix='/api')
app.register_blueprint(cards_bp, url_prefix='/api')

@app.route("/")
def index():
    response = requests.get("http://127.0.0.1:5000/api/boards")
    boards = data_handler.get_all_boards()
    return render_template("index.html", boards=boards)

@app.route('/remove-board', methods=['POST'])
def remove_board_request_page():
    try:
        board_id = request.form.get("title")
        data_handler.remove_board(board_id)
        return f"Usunięto '{board_id}' z listy tablic :)"
    except Exception as error:
        print(f"Wystąpił błąd: {str(error)}")
        return f"Wystąpił błąd podczas usuwania tablicy: {str(error)}"

if __name__ == "__main__":
    app()