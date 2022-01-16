from utils.http.base import BaseRequest

from flask import current_app

"""
天行接口
https://www.tianapi.com
"""


class TianxingRequest(BaseRequest):

    def __init__(self):
        self.host = 'http://api.tianapi.com'
        super().__init__()

    def _init_url(self):
        # 海外肺炎疫情
        self._ncovabroad_index_url = self._make_url('/ncovabroad/index')

    def get_ncovabroad_index(self, date: str = ''):
        params = {
            'key': current_app.config['TIANXING_API_KEY']
        }
        if date:
            params['date'] = date

        rv = self._do_request('GET', self._ncovabroad_index_url, params=params)

        return rv


tianxing_request = TianxingRequest()
