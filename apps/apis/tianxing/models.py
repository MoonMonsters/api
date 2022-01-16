from apps.extensions.db import db, BaseModel


class NCovabroad(BaseModel):
    """
    海外疫情数据
    """
    date = db.Column(db.String(16), nullable=False)
    data = db.Column(db.JSON, nullable=False)
