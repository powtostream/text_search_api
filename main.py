from elasticsearch import Elasticsearch
from pprint import pprint
import pandas as pd
from app import db
from app.api.models import Post


es = Elasticsearch("http://0.0.0.0:9200")
print(es.info().body)
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

print(df['rubrics'][0][0])

mappings = {
        "properties": {
            "id": {"type": "keyword"},
            "text": {"type": "text", "analyzer": "standard"},
    }
}

es.indices.create(index="posts", mappings=mappings)
es.indices.delete(index='posts')
posts = db.session.query(Post).all()

for post in posts:
    es.index(index="posts", id=post.id, document={'text': post.text})

# query = {}
# query = {
#     "bool": {
#         "must": {
#             "match_phrase": {
#                 "text": "Слив информации на пассивки",
#             }
#         }
#     }
# }
# resp = es.search(index='posts', body={'query': query})
# for hit in resp.get("hits").get('hits'):
#     print(hit.get("_id"))

# es.delete(index="posts", id=2)

# body = {
#     "query": {
#         "bool": {
#          "filter": {
#                 "term": {
#                    "_id": 250
#                 }
#             }
#         }
#     }
# }
# resp = es.search(index='posts', body=body)
# print(resp.get('hits').get('total').get('value'))
post = db.session.query(Post).get(2)
print(post.text)
db.session.delete(post)
db.session.commit()
post = db.session.query(Post).get(2)