__dict = dict(
    SDK_INVALID_REGION_ID='Can not find region to access.',
    SDK_SERVER_UNREACHABLE='Unable to connect server',
    SDK_INVALID_REQUEST='The request is not a valid AcsRequest.',
    SDK_UNKNOWN_SERVER_ERROR="Can not parse error message from server response.")


def get_msg(code):
    return __dict.get(code)
