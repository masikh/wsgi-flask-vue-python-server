from flask import jsonify, request, session, make_response
from PrivateClasses.Token import Token
from PrivateClasses.AESCipher import AESCipher
from PrivateClasses.Database import Database
from PrivateClasses.Users import Users
from Decorators.Authorization import authorize
from . import routes

""" Get token for accessing any API
"""


@routes.route('/api/login', methods=['POST'])
def api_login():
    """
        ---
        tags:
           - Authentication
        post:
          summary: request token
          description: This server
          consumes:
            - application/json
          produces:
            - application/json
          parameters:
            - name: body
              in: body
              required: true
              schema:
                type: object
                properties:
                  username:
                    type: string
                    example: test
                  password:
                    type: string
                    example: test
        responses:
          200:
            description: application token
            content:
              application/json:
                schema:
                  type: object
    """
    def error_response(error):
        payload = {'token': '', 'error': error}
        response = make_response(jsonify(payload))
        response.headers["Content-Type"] = "application/json"
        return response

    if request.method == 'POST':
        try:
            data = request.json
            username = data['username']
            password = data['password']

            database = Database()
            with database:
                stored_user = database.users({'username': username})
                if stored_user is None:
                    return error_response('Incorrect username/password')

                users = Users()
                checks_out = users.check(stored_user, password)
                if not checks_out:
                    return error_response('Incorrect username/password')

            tokens = Token(username)
            token = tokens.generate_auth_token()
            # Token can sometimes be a bytes object, convert to str
            if not isinstance(token, str):
                token = token.decode('utf-8')
            session['token'] = token
            session['username'] = username
            return jsonify({'token': token})
        except Exception as error:
            return error_response(error)


@routes.route('/api/logout', methods=['GET'])
def api_logout():
    try:
        session.pop('token')
        session.pop('username')
        return jsonify({'status': True, 'mesage': 'Session popped'})
    except KeyError:
        print('Logout: {"error": "No token in session"}')
    return jsonify({'status': False, 'message': 'Failed popping session'})


@authorize
@routes.route('/api/cipher', methods=['POST'])
def api_cipher():
    data = request.json
    aes = AESCipher(data=data['text'], password=data['password'])
    cipher_text = aes.encrypt_and_compress()
    return cipher_text


@authorize
@routes.route('/api/decipher', methods=['POST'])
def api_decipher():
    data = request.json
    aes = AESCipher(data=data['text'], password=data['password'])
    decipher_text = aes.uncompress_and_decrypt()
    return decipher_text
