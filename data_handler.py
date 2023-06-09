from data_manager import execute_select, execute_insert
from flask import redirect


def get_all_boards():
    result = execute_select("SELECT * FROM boards")
    return result

def add_board_to_database(name):
    print(name+'jest przekazywany')
    execute_insert("INSERT INTO boards (title) VALUES (%(name)s)" , variables = {'name': name})
    return redirect('/')
