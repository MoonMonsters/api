from flask import Blueprint

from apps.extensions.logger import logger

home = Blueprint("index", __name__, url_prefix="/")


@home.get('/')
def index():
    logger.info('home index')
    return "hello world"
