FROM python:3.11-alpine
LABEL maintainer="Actable AI"
LABEL description="Application for deploying and running Scrapy spiders."

ENV PYTHONUNBUFFERED 1

RUN set -ex && apk --no-cache --virtual .build-deps add build-base g++ bash curl gcc libgcc tzdata psutils linux-headers openssl-dev

RUN pip install pip==24.0
COPY ./requirements.txt /
RUN pip install -r requirements.txt

RUN mkdir /etc/scrapyd
RUN mkdir -p /opt/scrapyd/logs
COPY scrapyd.conf /etc/scrapyd/

EXPOSE 6800

WORKDIR /opt/scrapyd

CMD ["scrapyd"]