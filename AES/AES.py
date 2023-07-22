from Crypto.Cipher import AES
import binascii
import os

class AESAlgo:
    def __init__(self, key, msg):
        self.key = key
        self.msg = msg

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def setMsg(self, msg):
        self.msg = msg

    def getMsg(self):
        return self.msg

    """ encypt a  msg-string "msg" with a scret key "key"
    this function returns a tuple "(ciphertext, aesCipher.nonce, authTag)"
    where "ciphertext" is the encrypted text, "nonce" is the initialization vector,
    and "authTag" is the authentication tag.
    """
    def encrypt_AES_GCM(self, msg, key): 
        aesCipher = AES.new(key, AES.MODE_GCM)
        ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
        return (ciphertext, aesCipher.nonce, authTag)



    def decrypt_AES_GCM(self, msg, key):
        (ciphertext, nonce, authTag) = msg
        aesCipher = AES.new(key, AES.MODE_GCM, nonce)
        text = aesCipher.decrypt_and_verify(ciphertext, authTag)
        return text

