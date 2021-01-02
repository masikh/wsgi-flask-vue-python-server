from Crypto.Cipher import AES
from Crypto.Random import new as random
from hashlib import sha256
from pybase64 import b64encode, b64decode
import zlib


class AESCipher:
    def __init__(self, data=None, password=None, compression=False):
        self.blk_size = 16
        self.data = data
        self.key = sha256(password.encode()).digest()[:32]
        self.pad = lambda s: s + (self.blk_size - len(s) % self.blk_size) * chr(self.blk_size - len(s) % self.blk_size)
        self.un_pad = lambda s: s[:-ord(s[len(s) - 1:])]
        self.compression = compression

    def encrypt_and_compress(self):
        plain_text = self.pad(self.data)
        iv = random().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_OFB, iv)
        data = b64encode(iv + cipher.encrypt(plain_text.encode()))
        if self.compression is False:
            return data.decode("utf-8")
        compressed_data = zlib.compress(data)
        return compressed_data

    def uncompress_and_decrypt(self):
        try:
            data = self.data
            if self.compression is True:
                data = zlib.decompress(self.data)
            cipher_text = b64decode(data)
            iv = cipher_text[:self.blk_size]
            cipher = AES.new(self.key, AES.MODE_OFB, iv)
            return self.un_pad(cipher.decrypt(cipher_text[self.blk_size:])).decode()
        except:
            return 'Unable to decipher'
