import logging
from apps.extensions.request_id import request
from logging import FileHandler
import os

from flask import Flask
from flask_login import current_user

logger = logging.getLogger(__name__)


class CustomFormatter(logging.Formatter):

    def format(self, record):
        """
        自定义formatter, 加上request_id和user信息
        """
        record.request_id = request.id
        record.user = current_user.key

        return super().format(record)


def init_app(app: Flask):
    formatter = '[%(user)s][%(request_id)s][%(asctime)s][%(name)s] [%(levelname)s] (%(filename)s:%(funcName)s:%(lineno)d) %(message)s'
    level = logging.INFO
    log_formatter = CustomFormatter(formatter)
    stream = logging.StreamHandler()
    stream.setLevel(level)
    stream.setFormatter(log_formatter)

    info_handler = FileHandler(
        filename=os.path.join(app.config['LOGS_PATH'], 'api.log'),
        encoding='utf-8'
    )
    info_handler.setFormatter(log_formatter)

    logger.setLevel(level)
    logger.addHandler(stream)
    logger.addHandler(info_handler)
