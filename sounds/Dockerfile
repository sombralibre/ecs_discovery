FROM python:3.7-alpine

RUN apk update && \
    apk add gcc musl-dev linux-headers

COPY  . /
RUN pip install -r /requirements.txt

EXPOSE 8080

CMD ["uwsgi", "--yaml", "/uwsgi.yaml"]