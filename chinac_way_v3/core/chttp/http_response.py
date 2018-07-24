import urllib.request
from .http_request import HttpRequest


class HttpResponse(HttpRequest):
    def __init__(self, url, method='GET', headers={}, content=None):
        super(HttpResponse, self).__init__(url, method=method, headers=headers)
        self.__connection = None
        self.set_body(content)

    def get_response(self):
        request = urllib.request.Request(
            self.get_url(),
            data=self.get_body(),
            headers=self.get_headers(),
            method=self.get_method())
        response = urllib.request.urlopen(request)
        return response.getheaders(), response.read()

    def get_response_object(self):
        request = urllib.request.Request(
            self.get_url(),
            data=self.get_body(),
            headers=self.get_headers(),
            method=self.get_method())
        response = urllib.request.urlopen(request)
        return response.status, response.getheaders(), response.read()
