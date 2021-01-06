from flask import request
from PrivateClasses.AESCipher import AESCipher
from Decorators.Authorization import authorize
from . import routes


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
