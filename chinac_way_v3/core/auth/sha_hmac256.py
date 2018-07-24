import hmac
import hashlib
import base64


class ShaHmac256(object):
    def __init__(self):
        pass

    def sign_string(self, source, accessSecret):
        h = hmac.new(bytearray(accessSecret, 'utf-8'), bytearray(source, 'utf-8'), hashlib.sha256)
        signature = str(base64.encodebytes(h.digest()).strip(), "utf-8")
        return signature
