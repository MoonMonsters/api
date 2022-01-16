from apps.extensions.db import db, BaseModel
from flask_login import UserMixin


class UserInfo(BaseModel, UserMixin):
    key = db.Column(db.String(64), nullable=False)
    source = db.Column(db.String(64))
