from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({"message": "Hello, World!"})

@main.route('/hello/<name>')
def hello(name):
    return jsonify({"message": f"Hello, {name}!"})