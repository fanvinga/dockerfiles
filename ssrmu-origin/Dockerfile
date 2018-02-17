FROM python:alpine3.7

RUN apk --no-cache add libsodium-dev && \
    pip install cymysql && touch /etc/hosts.deny

ADD . /shadowsocksr

WORKDIR /shadowsocksr
CMD python server.py