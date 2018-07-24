from . import error_type


class ClientException(Exception):
    def __init__(self, code, msg):
        Exception.__init__(self)
        self.__error_type = error_type.ERROR_TYPE_CLIENT
        self.message = msg
        self.error_code = code

    def __str__(self):
        return "%s %s" % (self.error_code, self.message)

    def set_error_code(self, code):
        self.error_code = code

    def set_error_msg(self, msg):
        self.message = msg

    def get_error_type(self):
        return self.__error_type

    def get_error_code(self):
        return self.error_code

    def get_error_msg(self):
        return self.message


class ServerException(Exception):
    def __init__(self, code, msg, http_status=None, request_id=None):
        Exception.__init__(self)
        self.error_code = code
        self.message = msg
        self.__error_type = error_type.ERROR_TYPE_SERVER
        self.http_status = http_status
        self.request_id = request_id

    def __str__(self):
        return "HTTP Status: %s Error:%s %s RequestID: %s" % (
            str(self.http_status),
            self.error_code,
            self.message,
            self.request_id
        )

    def set_error_code(self, code):
        self.error_code = code

    def set_error_msg(self, msg):
        self.message = msg

    def get_error_type(self):
        return self.__error_type

    def get_error_code(self):
        return self.error_code

    def get_error_msg(self):
        return self.message

    def get_http_status(self):
        return self.http_status

    def get_request_id(self):
        return self.request_id
