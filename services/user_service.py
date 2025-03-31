from domain.user import User

def register_user(data):
    try:
        email = data.get("email")
        password = data.get("password")
        user = User(email, password)
        return {"message": "User registered successfully"}, 200
    except ValueError as e:
        return {"error": str(e)}, 400
    
def login_user(data):
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return {"error": "Missing email or password"}, 400

    # 模擬帳號驗證
    if email == "test@example.com" and password == "12345678":
        return {"message": "Login successful"}, 200
    else:
        return {"error": "Invalid credentials"}, 401
    
USER_DB = {}

from domain.user import User

def register_user(data):
    try:
        email = data.get("email")
        password = data.get("password")
        user = User(email, password)
        USER_DB[email] = user  # 儲存整個 User 實體
        return {"message": "User registered successfully"}, 200
    except ValueError as e:
        return {"error": str(e)}, 400

def login_user(data):
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return {"error": "Missing email or password"}, 400

    user = USER_DB.get(email)
    if user and user.check_password(password):
        return {"message": "Login successful"}, 200
    else:
        return {"error": "Invalid credentials"}, 401
