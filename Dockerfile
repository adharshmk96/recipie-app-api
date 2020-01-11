FROM python:3.8-alpine
MAINTAINER Adharsh

ENV PYTHONUNBUFFERED 1

COPY //requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

# RUN apk add --no-cache .build-deps build-base \
RUN apk add --no-cache jpeg-dev zlib-dev \
    && pip install Pillow

RUN pip install -r /requirements.txt
RUN pip freeze
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D execuser

RUN chown -R execuser:execuser /vol/
RUN chmod -R 755 /vol/web

USER execuser