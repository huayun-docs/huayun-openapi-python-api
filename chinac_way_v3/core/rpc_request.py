import time
import hashlib
import urllib.parse
from .. import config


class CRequest(object):
    def __init__(self, product, version, action):
        self.__product = product
        self.__version = version
        self.__action = action
        self.__region_id = None
        self.__method = 'GET'
        self.__protocol_type = 'http'
        self.__query_params = None
        self.__headers = {'x-sdk-client':'python/1.0'}
        self.__content = None

    def set_product(self, product):
        self.__product = product

    def get_product(self):
        return self.__product

    def set_version(self, version):
        self.__version = version

    def get_version(self):
        return self.__version

    def set_action(self, action):
        self.__action = action

    def get_action(self):
        return self.__action

    def set_protocol_type(self, protocol_type):
        self.__protocol_type = protocol_type

    def get_protocol_type(self):
        return self.__protocol_type

    def set_region_id(self, region_id):
        self.__region_id = region_id

    def get_region_id(self):
        return self.__region_id

    def set_method(self, method):
        self.__method = method

    def get_method(self):
        return self.__method

    def add_headers(self, k, v):
        if self.__headers is None:
            self.__headers = {}
        self.__headers[k] = v

    def set_headers(self, headers):
        self.__headers = headers

    def get_headers(self):
        return self.__headers

    def add_query_params(self, k, v):
        if self.__query_params is None:
            self.__query_params = {}
        self.__query_params[k] = v

    def get_query_params(self):
        return self.__query_params

    def set_content(self, content):
        self.__content = content

    def get_content(self):
        return self.__content


class RpcRequest(CRequest):
    def __init__(self, product, version, action):
        super(RpcRequest, self).__init__(product, version, action)
        self.__body_params = None
        self.__content_type = 'application/json;charset=UTF-8'
        self.__request_url = config.HTTP_REQUEST_URL
        self.__go_url = None
        self.__initialize()

    def __initialize(self):
        self.add_headers('Content-Type', self.__content_type)
        self.add_headers('Date', time.strftime("%Y-%m-%dT%H:%M:%S +0800", time.localtime()))

    def __prepareValue(self, value):
        if type(value) == bool:
            if value:
                return 'true'
            return 'false'
        return value

    def compose_url(self, signer, credential):
        if self.get_query_params() == None:
            params = {}
        else:
            params = {k: self.__prepareValue(v) for (k, v) in self.get_query_params().items()}
        params['Region'] = self.get_region_id()
        params['AccessKeyId'] = credential.get_access_key_id()
        params['Date'] = self.get_headers().get('Date')
        params['Action'] = self.get_action()
        params['Version'] = self.get_version()
        signature = self.__compute_signature(params, credential.get_access_secret(), signer)
        request_url = [self.__request_url.rstrip('/'), '/']
        if self.get_method() == 'POST':
            params['Signature'] = signature
            self.__body_params = params
        else:
            request_url.append('?')
            request_url.append(self.__pop_standard_urlencode(params))
            request_url.append('&Signature=')
            request_url.append(signature)

        self.__go_url = ''.join(request_url)

        return self.__go_url

    def __compute_signature(self, parameters, secret_key, signer):
        sign_string = [self.get_method(), "\n"]
        m = hashlib.md5()
        m.update(bytearray(self.__pop_standard_urlencode(parameters), 'utf-8')) 
        sign_string.append(m.hexdigest())
        sign_string.append("\n")
        sign_string.append(self.__content_type)
        sign_string.append("\n")
        sign_string.append(self.__pop_standard_urlencode_str(parameters['Date']))
        sign_string.append("\n")
        sign_string = ''.join(sign_string)
        signature = self.__pop_standard_urlencode_str(signer.sign_string(sign_string, secret_key))
        return signature

    def __pop_standard_urlencode(self, query):
        ret = urllib.parse.urlencode(query)
        ret = ret.replace('+', '%20')
        ret = ret.replace('*', '%2A')
        ret = ret.replace('%7E', '~')
        return ret

    def __pop_standard_urlencode_str(self, urlstr):
        urlstr = urllib.parse.quote(urlstr)
        urlstr = urlstr.replace('+', '%20')
        urlstr = urlstr.replace('*', '%2A')
        urlstr = urlstr.replace('%7E', '~')
        return urlstr

    def add_body_params(self, k, v):
        if self.__body_params is None:
            self.__body_params = {}
        self.__body_params[k] = v

    def set_body_params(self, params):
        self.__body_params = params

    def get_body_params(self):
        return self.__body_params

    def set_content_type(self, content_type):
        self.__content_type = content_type

    def get_content_type(self):
        return self.__content_type

    def set_request_url(self, url):
        self.__request_url = url

    def get_request_url(self):
        return self.__request_url

    def get_go_url(self):
        return self.__go_url
