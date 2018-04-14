FROM python:3.6

MAINTAINER Martin Cernek <martin.cernek@kiwi.com>

COPY requirements.txt srv/api/

COPY . /srv/api/
WORKDIR /srv/api

RUN pip install --no-cache-dir -r requirements.txt
