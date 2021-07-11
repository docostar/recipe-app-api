FROM python:3.9-alpine

ENV PYTHONBUFFERED 1

COPY ./requirnment.txt requirnment.txt
RUN pip install -r /requirnment.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app


RUN adduser -D user
USER user