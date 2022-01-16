from flask import request
from flask_login import login_user

from apps.account.models import UserInfo
from apps.extensions import response


def check_login():
    """
    鉴权
    """
    key = request.headers.get('key')
    if not key:
        return response.auth_failed('未携带鉴权信息')
    user = UserInfo.active_query().filter(UserInfo.key == key).first()
    if not user:
        return response.auth_failed('鉴权失败', {'key': key})

    # 设置登陆用户信息
    login_user(user)
