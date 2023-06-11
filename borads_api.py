from flask import Blueprint, jsonify, request, make_response
from data_manager import execute_select, execute_insert

boards_bp = Blueprint('boards_api', __name__)

@boards_bp.route("/boards")
def get_boards():
    result = execute_select("SELECT * FROM boards")
    return jsonify(result)

@boards_bp.route('/board', methods=['POST'])
def add_board():
    data = request.get_json()

    if not data or 'name' not in data:
        return make_response(jsonify({'error' : 'Bad Request (board name not specified)'}))
    result = execute_insert('INSERT INTO boards (title) VALUES (%s)', (data['name'],))
    return jsonify(result)


