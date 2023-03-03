import os

POSTGRES_DB = os.environ.get('POSTGRES_DB', default='posts')
POSTGRES_USER = os.environ.get('POSTGRES_USER', default='admin')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', default='admin')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', default='db')
POSTGRES_PORT = os.environ.get('POSTGRES_HOST', default='5432')

ELASTICSEARCH_HOST = os.environ.get(
    'ELASTICSEARCH_HOST', default='elasticsearch')
ELASTICSEARCH_PORT = os.environ.get('ELASTICSEARCH_PORT', default='9200')

ELASTICSEARCH_URI = f"http://{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}"
# ELASTICSEARCH_URI = "http://localhost:9200"

SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# SQLALCHEMY_DATABASE_URI = "postgresql://admin:admin@localhost:7777/posts"
