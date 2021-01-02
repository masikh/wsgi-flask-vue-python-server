import Configuration
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from PrivateClasses.Database import Database


class Token:
    def __init__(self, username=None):
        self.username = username

    def generate_auth_token(self, expiration=600):
        s = Serializer(Configuration.global_parameters['app'].config['SECRET_KEY'], expires_in=expiration)
        token = s.dumps({'id': self.username})
        database = Database()
        with database:
            user = database.users({'username': self.username})
            user['token'] = token
            database.users(user, add=True)
        return token

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(Configuration.global_parameters['app'].config['SECRET_KEY'])
        try:
            data = s.loads(token)
            database = Database()
            with database:
                result = database.users({'username': data['id']})
            username = result['username']
            return username
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        except Exception as error:
            return None
