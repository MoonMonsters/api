import requests
import traceback

from apps.extensions.logger import logger


class BaseRequest(object):

    def __init__(self):
        self._session = requests.Session()
        self._init_url()

    def _init_url(self):
        """
        初始化url信息
        """
        raise NotImplementedError

    def _make_url(self, uri):
        """
        拼接url
        """

        host = getattr(self, 'host')
        if not host:
            raise Exception('未设置host')
        return f'{host}{uri}'

    def _do_request(self, method, url, params=None, data=None, _json=None, headers=None):
        logger.info(f'method: {method}, url: {url}, params: {params}, data: {data}, json: {_json}, headers: {headers}')
        try:
            resp = self._session.request(method, url, params=params, data=data, json=_json, headers=headers)
            rv = resp.json()
            logger.info(f'rv: {rv}')

            return rv
        except:
            logger.error(f'error: {traceback.format_exc()}')
            return {}
