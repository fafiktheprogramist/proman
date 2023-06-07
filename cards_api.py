from flask import Blueprint, jsonify
from data_manager import execute_select

cards_bp = Blueprint('cards_api', __name__)

@cards_bp.route("/cards")
def get_cards():
    result = execute_select("SELECT * FROM cards")
    return jsonify(result)

