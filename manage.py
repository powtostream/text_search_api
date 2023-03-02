import pandas as pd
from elasticsearch import Elasticsearch
from flask_migrate import Migrate, MigrateCommand

from flask_script import Manager

from app import app, db, es

from app.api.models import Post

manager = Manager(app)

migrate = Migrate(app, db, compare_type=True)
manager.add_command("db", MigrateCommand)


@manager.command
def add_data_to_db():
    df = pd.read_csv('posts.csv')
    df['rubrics'] = df['rubrics'].replace(
        to_replace=r"['\[\] ]", value='', regex=True
    )
    df['rubrics'] = df['rubrics'].str.split(",")
    dict_rows = df.to_dict(orient='records')

    for row in dict_rows:
        new_post = Post(**row)
        db.session.add(new_post)
    db.session.commit()


@manager.command
def create_index():
    mappings = {
        "properties": {
            "id": {"type": "keyword"},
            "text": {"type": "text", "analyzer": "standard"},
        }
    }

    es.indices.create(index="posts", mappings=mappings)


@manager.command
def add_data_to_index():
    posts = db.session.query(Post).all()

    for post in posts:
        es.index(index="posts", id=post.id, document={'text': post.text})


if __name__ == "__main__":
    manager.run()
