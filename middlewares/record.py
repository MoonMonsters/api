from flask import request

from apps.extensions.logger import logger


def record_every_request():
    """
    记录下每一个请求
    """
    method = request.method
    params = {}
    if method == 'GET':
        params = dict(request.args)
    elif method == 'POST':
        params = dict(request.get_json())

    logger.info(f'api record, method: {method}, url: {request.path}, params: {params}')
