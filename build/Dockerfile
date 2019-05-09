FROM python:3.7-alpine3.7

ARG project_dir=app/

WORKDIR $project_dir
ADD requirements.txt $project_dir
RUN pip install -r requirements.txt
