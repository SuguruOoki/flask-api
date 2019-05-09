FROM python:3.7-alpine3.7

MAINTAINER Suguru Ohki

ARG project_dir=/app/

WORKDIR $project_dir
RUN pip install -U pip
RUN pip install -U --no-cache-dir -r requirements.txt \
 && apk add --no-cache openssl \
 && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz
