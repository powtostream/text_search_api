# Search Text API
API for searching for specific text in posts \
Volumes are disabled, to activate uncomment corresponding lines in docker-compose-elastic.yml
### Build
```bash
docker-compose -f docker-compose-elastic.yml build
```
### Run
```bash
docker-compose -f docker-compose-elastic.yml up
```
DB migration, dumping data from posts.csv, creating index for elastic and adding data from db to index are executed each time before run.
### Environment variables
All necessary variables are set by default \
Environment variables need to be put in .env file in root directory

POSTGRES_DB - database name \
POSTGRES_USER - database user \
POSTGRES_PASSWORD - database user password \
POSTGRES_HOST - database host ("db" if run in docker) \
POSTGRES_PORT - database port ("5432" if run in docker) \ 

ELASTICSEARCH_HOST - elasticsearch host ("elasticsearch" if run in docker) \
ELASTICSEARCH_PORT - elasticsearch port ("9200" if run in docker)