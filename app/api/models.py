from sqlalchemy import func

from app import db


class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer(), primary_key=True)
    rubrics = db.Column(db.ARRAY(db.String()), nullable=True)
    text = db.Column(db.UnicodeText(), nullable=False)
    created_date = db.Column(
        db.DateTime(), nullable=True, server_default=func.now()
    )
