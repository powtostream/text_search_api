import http

from flask import Blueprint, request
from marshmallow import ValidationError

from app import es, db
from app.api.models import Post
from app.api.schemas import (
    MatchPhraseSchema, ResponseSchema, ListPostSchema, PostIdSchema
)

bp = Blueprint("text_search", __name__, url_prefix="/")


@bp.route("search/", methods=['POST'])
def search():
    raw_data = request.json

    try:
        valid_data = MatchPhraseSchema().load(raw_data)
    except ValidationError as err:
        return (
            ResponseSchema().dump(
                {"message": f"Данные введены неверно: {err}"}
            ),
            http.HTTPStatus.BAD_REQUEST
        )

    match_phrase = valid_data.get("match_phrase")
    query = {
        "bool": {
            "must": {
                "match_phrase": {
                    "text": match_phrase,
                }
            }
        }
    }
    resp = es.search(index='posts', body={'query': query})

    id_list = list()
    for hit in resp.get("hits").get('hits'):
        id_list.append(hit.get("_id"))

    posts = (db.session.query(Post)
             .filter(Post.id.in_(id_list))
             .order_by(db.desc(Post.created_date))
             .limit(20).all())

    total = len(posts)

    return ListPostSchema().dump(
        {"posts": posts, "total_posts": total}
    ), http.HTTPStatus.OK


@bp.route("delete/<post_id>/", methods=['DELETE'])
def delete(post_id):

    error = PostIdSchema().validate({"post_id": post_id})

    if error:
        return ResponseSchema().dump(
            {"message": f"Данные введены неверно: {error}"}
        ), http.HTTPStatus.BAD_REQUEST

    post_id = int(post_id)

    try:
        es.delete(index="posts", id=post_id)

        post = db.session.query(Post).get(post_id)
        db.session.delete(post)
        db.session.commit()

    except Exception as exc:
        db.session.rollback()
        return ResponseSchema().dump(
            {"message": f"Ошибка удаления: {exc}"}
        ), http.HTTPStatus.CONFLICT

    return ResponseSchema().dump(
        {"message": "Пост успешно удалён"}
    ), http.HTTPStatus.OK