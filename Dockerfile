FROM python:3.7-alpine3.7

MAINTAINER Suguru Ohki

ARG project_dir=/app/

WORKDIR $project_dir
RUN pip install -U pip
ADD requirements.txt $project_dir
RUN pip install -r requirements.txt
