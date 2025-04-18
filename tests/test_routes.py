def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}

def test_hello(client):
    response = client.get('/hello/Jeff')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, Jeff!"}

def test_calc_addition(client):
    response = client.get('/calc?x=3&y=4')
    assert response.status_code == 200
    assert response.json == {"result": 7}

def test_calc_missing_param(client):
    response = client.get('/calc?x=3')  # 缺少 y
    assert response.status_code == 400
    assert response.json == {"error": "Missing x or y"}

def test_calc_invalid_param(client):
    response = client.get('/calc?x=3&y=abc')  # y 不是數字
    assert response.status_code == 400
    assert response.json == {"error": "x and y must be numbers"}


def test_divide_success(client):
    response = client.get('/divide?x=10&y=2')
    assert response.status_code == 200
    assert response.json == {"result": 5.0}

def test_divide_zero(client):
    response = client.get('/divide?x=10&y=0')
    assert response.status_code == 400
    assert response.json == {"error": "Cannot divide by zero"}

def test_divide_missing_param(client):
    response = client.get('/divide?x=10')
    assert response.status_code == 400
    assert response.json == {"error": "Missing x or y"}

def test_divide_invalid_param(client):
    response = client.get('/divide?x=ten&y=2')
    assert response.status_code == 400
    assert response.json == {"error": "x and y must be numbers"}


def test_register_success(client):
    response = client.post('/register', json={
        "email": "test@example.com",
        "password": "12345678"
    })
    assert response.status_code == 200
    assert response.json == {"message": "User registered successfully"}

def test_register_invalid_email(client):
    response = client.post('/register', json={
        "email": "invalid",
        "password": "12345678"
    })
    assert response.status_code == 400
    assert response.json == {"error": "Invalid email format"}

def test_register_short_password(client):
    response = client.post('/register', json={
        "email": "test@example.com",
        "password": "123"
    })
    assert response.status_code == 400
    assert response.json == {"error": "Password too short (min 8)"}

def test_login_success(client):
    response = client.post('/login', json={
        "email": "test@example.com",
        "password": "12345678"
    })
    assert response.status_code == 200
    assert response.json == {"message": "Login successful"}

def test_login_wrong_password(client):
    response = client.post('/login', json={
        "email": "test@example.com",
        "password": "wrongpass"
    })
    assert response.status_code == 401
    assert response.json == {"error": "Invalid credentials"}

def test_login_missing_fields(client):
    response = client.post('/login', json={
        "email": ""
    })
    assert response.status_code == 400
    assert response.json == {"error": "Missing email or password"}    


def test_login_success_with_hashed_password(client):
    client.post('/register', json={
        "email": "secure@example.com",
        "password": "strongpass123"
    })

    response = client.post('/login', json={
        "email": "secure@example.com",
        "password": "strongpass123"
    })

    assert response.status_code == 200
    assert response.json == {"message": "Login successful"}

"""註冊時把使用者存到「SQLite 資料庫」"""
def test_register_and_login_with_db(client): 
    # 註冊
    response = client.post('/register', json={
        "email": "dbuser@example.com",
        "password": "supersecure"
    })
    assert response.status_code == 200

    # 登入
    response = client.post('/login', json={
        "email": "dbuser@example.com",
        "password": "supersecure"
    })
    assert response.status_code == 200
    assert response.json == {"message": "Login successful"}