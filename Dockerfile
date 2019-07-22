FROM python:3.7-alpine

RUN apk add --update \
    build-base \
    linux-headers \
    postgresql-dev \
    && rm -rf /var/cache/apk/*

WORKDIR /app

COPY ./requirements/local.txt /app/requirements/local.txt

RUN pip install --no-cache-dir -r /app/requirements/local.txt

COPY . .

CMD python manage.py migrate --noinput && \
    python manage.py collectstatic --clear --noinput && \
    uwsgi uwsgiconf/docker.ini
