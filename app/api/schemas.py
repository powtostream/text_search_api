from app import ma
from app.api.helpers import validate_post_id


class MatchPhraseSchema(ma.Schema):
    match_phrase = ma.String(required=True, example="конкурс")


class PostSchema(ma.Schema):
    id = ma.Integer(example=11)
    rubrics = ma.List(
        ma.String(),
        example=['VK-1603736028819866', 'VK-49725783613', 'VK-92549753485'])
    text = ma.String(example="Конкурс на НОВЫЙ СКИН ‼")
    created_date = ma.DateTime(example="2019-12-29 20:14:28")


class ListPostSchema(ma.Schema):
    total_posts = ma.Integer(example=3)
    posts = ma.List(ma.Nested(PostSchema))


class ResponseSchema(ma.Schema):
    message = ma.String(example="Данные введены неверно")


class PostIdSchema(ma.Schema):
    post_id = ma.Integer(
        required=True, validate=[validate_post_id], example=23)
