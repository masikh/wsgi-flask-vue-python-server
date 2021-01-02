import os
import hashlib
from PrivateClasses.Database import Database


class Users:
    def __init__(self):
        self.database = Database()

    @staticmethod
    def hash_password(clear_password):
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', clear_password.encode('utf-8'), salt, 100000)
        hash = salt + key
        return hash

    @staticmethod
    def check(payload, clear_password):
        salt_from_storage = payload['password_hash'][:32]  # 32 is the length of the salt
        key_from_storage = payload['password_hash'][32:]

        new_key = hashlib.pbkdf2_hmac(
            'sha256',
            clear_password.encode('utf-8'),  # Convert the password to bytes
            salt_from_storage,
            100000
        )

        if new_key == key_from_storage:
            return True
        return False

    def add(self, username, clear_password):
        with self.database:
            self.database.users({'username': username, 'password_hash': self.hash_password(clear_password)}, add=True)

    def delete(self, username):
        with self.database:
            self.database.users({'username': username}, delete=True)
