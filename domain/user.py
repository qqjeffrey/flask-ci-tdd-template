import re
import bcrypt

class User:
    def __init__(self, email, password):
        if not self.is_valid_email(email):
            raise ValueError("Invalid email format")
        if len(password) < 8:
            raise ValueError("Password too short (min 8)")

        self.email = email
        self.hashed_password = self.hash_password(password)

    def is_valid_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)
    
    def hash_password(self, password):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    def check_password(self, raw_password):
        return bcrypt.checkpw(raw_password.encode("utf-8"), self.hashed_password)