from datetime import date

from apps.apis.tianxing.models import NCovabroad
from apps.extensions import response
from apps.extensions.logger import logger
from utils.http.tianxing import tianxing_request
from utils.datetime_format import date_to_str

"""
海外疫情接口
http://api.tianapi.com/ncovabroad/index?key=APIKEY
"""


def _ncovabroad_date_data(_date) -> NCovabroad:
    return NCovabroad.active_query().filter(NCovabroad.date == _date).first()


def ncovabroad_api(_date):
    """
    海外疫情数据
    """
    if not _date:
        _date = date_to_str(date.today())
    instance = _ncovabroad_date_data(_date)
    if instance:
        result = instance.data
    else:
        rv = tianxing_request.get_ncovabroad_index(_date)
        if not rv:
            logger.error(f'服务器异常, {date}')
            return response.server_error('服务器异常')
        if rv.get('code', 0) != 200:
            logger.error(f'接口响应异常, {date}')
            return response.bad_request('接口响应异常')

        result = rv['newslist']
        nc = NCovabroad()
        nc.date = _date
        nc.data = result
        nc.save()

    return response.success('success', {'list': result})
