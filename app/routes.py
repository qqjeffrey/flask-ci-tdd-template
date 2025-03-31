from flask import Blueprint, jsonify
from services.calc_service import divide
from services.user_service import register_user

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({"message": "Hello, World!"})

@main.route('/hello/<name>')
def hello(name):
    return jsonify({"message": f"Hello, {name}!"})

@main.route('/calc')
def calc():
    from flask import request

    x = request.args.get("x")
    y = request.args.get("y")

    if x is None or y is None:
        return jsonify({"error": "Missing x or y"}), 400

    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return jsonify({"error": "x and y must be numbers"}), 400

    return jsonify({"result": x + y})

@main.route('/divide')
def divide_route():
    from flask import request

    x = request.args.get("x")
    y = request.args.get("y")

    results, status = divide(x, y)
    return jsonify(results), status


@main.route('/register', methods=['POST'])
def register():
    from flask import request
    data = request.get_json()
    result, status = register_user(data)
    return jsonify(result), status

@main.route('/login', methods=['POST'])
def login():
    from flask import request
    from services.user_service import login_user

    data = request.get_json()
    result, status = login_user(data)
    return jsonify(result), status