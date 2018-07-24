import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from ..auth.credential import Credential
from ..auth.sha_hmac256 import ShaHmac256


class Profile(object):
    def __init__(self, region_id, access_key_id, access_secret):
        self.__region_id = region_id
        self.__signer = None
        self.__credential = Credential(access_key_id, access_secret)

    def get_signer(self):
        if self.__signer == None:
            self.__signer = ShaHmac256()

        return self.__signer

    def get_credential(self):
        return self.__credential

    def get_region_id(self):
        return self.__region_id
