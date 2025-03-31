import sqlite3
from domain.user import User

DB_PATH = "users.db"

# 初始化資料表（第一次會自動建）
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            email TEXT PRIMARY KEY,
            hashed_password BLOB
        )
    ''')
    conn.commit()
    conn.close()

# 新增使用者
def save_user(user: User):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (email, hashed_password) VALUES (?, ?)', 
                   (user.email, user.hashed_password))
    conn.commit()
    conn.close()

# 依 email 取得使用者
def get_user_by_email(email) -> User | None:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT email, hashed_password FROM users WHERE email = ?', (email,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        user = User.__new__(User)  # 不呼叫 __init__（因為不需要驗證）
        user.email = row[0]
        user.hashed_password = row[1]
        return user
    return None
