FROM python:3.10.7-buster

RUN set -eux; \
        rm /etc/localtime; \
        ln -s /usr/share/zoneinfo/Europe/Moscow /etc/localtime; \
        date

COPY requirements.txt /app/requirements.txt
RUN set -eux; \
        pip install --no-cache-dir -r /app/requirements.txt; \
        rm /app/requirements.txt

ADD . app

COPY entrypoint_scripts/ .

RUN set -eux; \
        chmod 0700 ./docker-entrypoint.sh; \
        chmod 0700 ./wait-for-it.sh

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "--host=0.0.0.0"]
