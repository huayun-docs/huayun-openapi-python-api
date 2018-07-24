import urllib
import warnings
import http.client
from cexception.exceptions import ClientException
from cexception.exceptions import ServerException
from cexception import error_code, error_msg
from chttp.http_response import HttpResponse

warnings.filterwarnings('once', category=DeprecationWarning)

try:
    import json
except ImportError:
    import simplejson as json


class Client(object):
    def __init__(self, profile, auto_retry=False, max_retry_time=1, user_agent=None):
        self.__profile = profile
        self.__auto_retry = auto_retry
        self.__max_retry_num = max_retry_time
        self.__user_agent = user_agent

    def is_auto_retry(self):
        return self.__auto_retry

    def get_max_retry_num(self):
        return self.__max_retry_num

    def get_user_agent(self):
        return self.__user_agent

    def set_max_retry_num(self, num):
        self.__max_retry_num = num

    def set_auto_retry(self, flag):
        self.__auto_retry = flag

    def set_user_agent(self, agent):
        self.__user_agent = agent

    def get_response(self, request, signer=None, credential=None):
        status, headers, body = self.__do_action(request, signer, credential)

        tast_id = None

        try:
            body_obj = json.loads(body)
            tast_id = body_obj.get('TaskId')
        except ValueError:
            pass

        if status < http.client.OK or status >= http.client.MULTIPLE_CHOICES:
            server_error_code, server_error_message = self.__parse_error_response_body(body)
            raise ServerException(
                server_error_code,
                server_error_message,
                http_status=status,
                request_id=tast_id)

        return body

    def __parse_error_response_body(self, response_body):
        try:
            body_obj = json.loads(response_body)
            if 'Code' in body_obj and 'Message' in body_obj:
                return (body_obj['Code'], body_obj['Message'])
            else:
                return (
                    error_code.SDK_UNKNOWN_SERVER_ERROR,
                    error_msg.get_msg('SDK_UNKNOWN_SERVER_ERROR'))
        except ValueError:
            return (error_code.SDK_UNKNOWN_SERVER_ERROR,
                    error_msg.get_msg('SDK_UNKNOWN_SERVER_ERROR'))

    def __do_action(self, request, signer, credential):
        if self.__profile == None and (
            signer == None or credential == None or request.get_region_id() == None
            ):
            raise ClientException('No active profile found.', 'SDK.InvalidProfile')

        if signer == None:
            signer = self.__profile.get_signer()

        if credential == None:
            credential = self.__profile.get_credential()

        request = self.__prepare_request(request)

        request_url = request.compose_url(signer, credential)

        http_response = self.__make_http_response(request)

        try:
            status, headers, body = http_response.get_response_object()
            return status, headers, body
        except IOError as e:
            raise ClientException(
                error_code.SDK_SERVER_UNREACHABLE,
                error_msg.get_msg('SDK_SERVER_UNREACHABLE') + ': ' + str(e))
        except AttributeError:
            raise ClientException(
                error_code.SDK_INVALID_REQUEST,
                error_msg.get_msg('SDK_INVALID_REQUEST'))

    def __make_http_response(self, request):
        if request.get_body_params() is not None:
            body = urllib.parse.urlencode(request.get_body_params())
            request.set_content(body)
        content = request.get_content()
        header = request.get_headers()
        if self.__user_agent is not None:
            header['User-Agent'] = self.__user_agent
        if header is None:
            header = {}

        response = HttpResponse(request.get_go_url(), request.get_method(), header, content)
        if request.get_body_params() is not None:
            body = urllib.parse.urlencode(request.get_body_params())
            response.set_content(body, 'utf-8')
        return response

    def __prepare_request(self, request):
        if request.get_region_id() == None:
            request.set_region_id(self.__profile.get_region_id())

        if request.get_method() == None:
            request.set_method('GET')

        return request
