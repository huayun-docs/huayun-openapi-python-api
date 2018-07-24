class Credential(object):
    def __init__(self, access_key_id, access_secret):
        self.__access_key_id = access_key_id
        self.__access_secret = access_secret

    def set_access_key_id(self, access_key_id):
        self.__access_key_id = access_key_id

    def set_access_secret(self, access_secret):
        self.__access_secret = access_secret

    def get_access_key_id(self):
        return self.__access_key_id

    def get_access_secret(self):
        return self.__access_secret
