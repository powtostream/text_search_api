from app import ma
from app.api.helpers import validate_post_id


class MatchPhraseSchema(ma.Schema):
    match_phrase = ma.String(required=True)


class PostSchema(ma.Schema):
    id = ma.Integer()
    rubrics = ma.List(ma.String())
    text = ma.String()
    created_date = ma.DateTime()


class ListPostSchema(ma.Schema):
    total_posts = ma.Integer()
    posts = ma.List(ma.Nested(PostSchema))


class ResponseSchema(ma.Schema):
    message = ma.String()


class PostIdSchema(ma.Schema):
    post_id = ma.Integer(required=True, validate=[validate_post_id])
