from flask import Flask
from flask_login import LoginManager

from apps.account.models import UserInfo

manager = LoginManager()
manager.login_view = 'login'
manager.login_message_category = 'info'
manager.login_message = 'Access denied.'


@manager.user_loader
def load_user(key: str):
    return UserInfo.active_query().filter(UserInfo.id == key).first()


def init_app(app: Flask):
    manager.init_app(app)
