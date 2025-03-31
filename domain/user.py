import re

class User:
    def __init__(self, email, password):
        if not self.is_valid_email(email):
            raise ValueError("Invalid email format")
        if len(password) < 8:
            raise ValueError("Password too short (min 8)")

        self.email = email
        self.password = password

    def is_valid_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)