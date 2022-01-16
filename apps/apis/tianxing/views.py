from flask import Blueprint, request

from apps.apis.tianxing import services

tianxing = Blueprint('tianxing', __name__, url_prefix='/tianxing')


@tianxing.get('ncovabroad/index')
def ncovabroad():
    """
    海外疫情接口
    """
    date = request.args.get('date', '', str)

    return services.ncovabroad_api(date)
