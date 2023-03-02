from elasticsearch import Elasticsearch
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import config

app = Flask(__name__, static_url_path="/static")
app.config.from_object("config")

db = SQLAlchemy(app)
ma = Marshmallow(app)
es = Elasticsearch(config.ELASTICSEARCH_URI)

from app.api.views import bp
app.register_blueprint(bp)
