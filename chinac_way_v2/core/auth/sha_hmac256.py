import hmac
import hashlib
import base64


class ShaHmac256(object):
    def __init__(self):
        pass

    def sign_string(self, source, accessSecret):
        h = hmac.new(accessSecret, source, hashlib.sha256)
        signature = base64.encodestring(h.digest()).strip()
        return signature
