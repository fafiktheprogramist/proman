from flask import Flask, render_template
from borads_api import boards_bp
from cards_api import cards_bp
import requests
from flask import Blueprint, jsonify, request, make_response
from data_manager import execute_select, execute_insert
import data_handler


app = Flask(__name__)
app.config['DEBUG'] = True

# app.register_blueprint(boards_bp, url_prefix='/api')
# app.register_blueprint(cards_bp, url_prefix='/api')

@app.route("/")
def index():
    # response = requests.get("http://127.0.0.1:5000/api/boards")
    boards = data_handler.get_all_boards()
    return render_template("index.html", boards=boards)

@app.route('/board', methods=['POST','GET'])
def add_board():
    #data = request.get_json()
    name = request.form.get('name')
    data_handler.add_board_to_database(name)
    print(name)
    

    # if 'name' in data:
    #     return make_response(jsonify({'error' : 'Bad Request (board name already in use)'}))
    
    # return jsonify({'message' : f'Submitted board with name {data["name"]}'})

if __name__ == "__main__":
    app()