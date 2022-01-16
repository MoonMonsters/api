import os
import yaml

from flask import Flask, Blueprint


def create_app():
    _app = Flask(__name__)

    _init_directory_config(_app)
    _init_config(_app)
    _init_extensions(_app)
    _register_api(_app)
    _register_middlewares(_app)

    return _app


def _init_extensions(app: Flask):
    from apps.extensions import db
    from apps.extensions import logger
    from apps.extensions import request_id
    from apps.extensions import login

    db.init_app(app)
    logger.init_app(app)
    request_id.init_app(app)
    login.init_app(app)


def _init_config(app: Flask):
    def _read_yaml(path):
        with open(path, 'rb') as fp:
            cf = fp.read()
            return yaml.load(cf, yaml.FullLoader)

    local_file = _read_yaml(os.path.join(app.config['CONF_PATH'], 'local.yaml'))
    app.config.update(local_file)


def _init_directory_config(app: Flask):
    """
    添加目录的路径信息
    """
    # 项目根目录
    app.config['PROJECT_PATH'] = os.path.dirname(app.instance_path)
    app.config['LOGS_PATH'] = os.path.join(app.config['PROJECT_PATH'], 'logs')
    app.config['CONF_PATH'] = os.path.join(app.config['PROJECT_PATH'], 'conf')


def _register_api(app: Flask):
    from apps.apis.home import home
    from apps.apis.tianxing.views import tianxing

    v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
    v1.register_blueprint(home)
    v1.register_blueprint(tianxing)

    app.register_blueprint(v1)


def _register_middlewares(app: Flask):
    from middlewares.auth import check_login
    from middlewares.record import record_every_request

    @app.before_request
    def _check_login():
        return check_login()

    @app.before_request
    def _record_every_request():
        record_every_request()
