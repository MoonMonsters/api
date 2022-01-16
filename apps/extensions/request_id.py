from flask import Flask
from flask_request_id import RequestID

request = RequestID()


def init_app(app: Flask):
    request.init_app(app)
