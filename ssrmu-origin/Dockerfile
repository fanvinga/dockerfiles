FROM python:alpine3.7

RUN apk --no-cache add libsodium-dev && \
    pip install cymysql

ADD . /shadowsocksr

WORKDIR /shadowsocksr
CMD python server.py