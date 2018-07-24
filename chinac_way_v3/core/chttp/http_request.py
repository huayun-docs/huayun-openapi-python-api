class HttpRequest(object):
    def __init__(self, url, method=None, headers={}):
        self.__url = url
        self.__method = method
        self.__content_type = ''
        self.__content = ''
        self.__encoding = ''
        self.__headers = headers
        self.__body = None

    def get_body(self):
        return self.__body

    def set_body(self, body):
        self.__body = body

    def get_url(self):
        return self.__url

    def set_url(self, url):
        self.__url = url

    def get_encoding(self):
        return self.__encoding

    def set_encoding(self, encoding):
        self.__encoding = encoding

    def get_content_type(self):
        return self.__content_type

    def set_content_type(self, content_type):
        self.__content_type = content_type

    def get_method(self):
        return self.__method

    def set_method(self, method):
        self.__method = method

    def get_content(self):
        return self.__content

    def get_header_value(self, name):
        return self.__headers[name]

    def put_header_parameter(self, key, value):
        if key is not None and value is not None:
            self.__headers[key] = value

    def md5_sum(self, content):
        return helper.md5_sum(content)

    def set_content(self, content, encoding):
        if content is None:
            self.__content_type = None
            self.__content = None
            self.__encoding = None
            return
        self.__content = content
        self.__encoding = encoding

    def get_headers(self):
        return self.__headers
