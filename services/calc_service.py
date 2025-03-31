def divide(x_str, y_str):
    if x_str is None or y_str is None:
        return {"error": "Missing x or y"}, 400

    try:
        x = int(x_str)
        y = int(y_str)
    except ValueError:
        return {"error": "x and y must be numbers"}, 400

    if y == 0:
        return {"error": "Cannot divide by zero"}, 400

    return {"result": x / y}, 200
