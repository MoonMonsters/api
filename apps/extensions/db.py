from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def init_app(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 软删除使用, False表示已删除
    active = db.Column(db.Boolean, default=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)

    @classmethod
    def active_query(cls):
        """
        默认填写了active == 1这选项
        """
        return cls.query.filter(cls.active == 1)

    def save(self):
        db.session.add(self)
        db.session.commit()
