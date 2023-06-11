from flask import Blueprint, jsonify, request, make_response, abort
from data_manager import execute_select, execute_insert, execute_update

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

@boards_bp.route('/board/<id>', methods =['PATCH'])
def rename_board(id):
    data = request.get_json()

    if not data or 'name' not in data:
        return make_response(jsonify({'error' : 'Bad Request (board name not specified)'}))
    
    result = execute_select("SELECT * FROM boards WHERE id = %(id)s", variables={'id': id})
    if len(result) < 1:
        abort(404)
    statement = 'UPDATE boards SET title = %(new_title)s WHERE id = %(board_id)s'
    variables = {'new_title': data['name'], 'board_id': id}
    data = execute_update(statement, variables)
    return jsonify(data)

    





