FROM python:3.7-alpine
LABEL maintainer="Yeon Woo Park"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /ezmeetup
WORKDIR /ezmeetup
COPY ./ezmeetup /ezmeetup

# Security purpose
RUN adduser -D user
USER user