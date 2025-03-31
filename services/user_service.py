from domain.user import User

def register_user(data):
    try:
        email = data.get("email")
        password = data.get("password")
        user = User(email, password)
        return {"message": "User registered successfully"}, 200
    except ValueError as e:
        return {"error": str(e)}, 400
