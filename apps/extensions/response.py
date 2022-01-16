class Code(object):
    SUCCESS = 20000
    NOT_AUTHENTICATED = 30000
    BAD_REQUEST = 40000
    SERVER_ERROR = 50000


def _to_response(code, msg='', data=None):
    return {
        'code': code,
        'msg': msg,
        'data': data
    }


def success(msg, data=None):
    return _to_response(Code.SUCCESS, msg, data)


def auth_failed(msg, data=None):
    return _to_response(Code.NOT_AUTHENTICATED, msg, data)


def bad_request(msg, data=None):
    return _to_response(Code.BAD_REQUEST, msg, data)


def server_error(msg, data=None):
    return _to_response(Code.SERVER_ERROR, msg, data)
