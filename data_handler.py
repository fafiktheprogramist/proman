from data_manager import execute_select, execute_insert, execute_delete
from flask import redirect

def get_all_boards():
    result = execute_select("SELECT * FROM boards")
    return result

def add_board_to_database(name):
    execute_insert("INSERT INTO boards (title) VALUES (%(name)s)" , variables = {'name': name})
    return redirect('/')

def remove_board(board_id):
    execute_delete("DELETE FROM boards WHERE id = %(id)s", variables={'id': board_id})