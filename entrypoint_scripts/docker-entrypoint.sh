#!/bin/bash

set -e

cd app

echo 'upgrading db'
../wait-for-it.sh db:5432 -t 30 -- echo "database is ready"
python manage.py db upgrade

echo 'adding data to db'
python manage.py add_data_to_db

echo 'creating index'
../wait-for-it.sh elasticsearch:9200 -t 120 -- echo "elastic cluster is ready"
python manage.py create_index

echo 'adding data to index'
python manage.py add_data_to_index

echo "$@"
exec "$@"