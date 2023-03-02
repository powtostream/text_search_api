from marshmallow import ValidationError

from app import db, es
from app.api.models import Post


def validate_post_id(post_id):
    """
    Поднимает ValidationError, если пост не найден
    """
    db_post = db.session.query(Post).get(post_id)

    if not db_post:
        raise ValidationError(
            "Пост с указанным id не найден в базе данных"
        )
    body = {
        "query": {
            "bool": {
                "filter": {
                    "term": {
                        "_id": post_id
                    }
                }
            }
        }
    }
    resp = es.search(index='posts', body=body)

    if resp.get('hits').get('total').get('value') == 0:
        raise ValidationError(
            "Пост с указанным id не найден в индексе"
        )
