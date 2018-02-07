FROM alpine:3.7

RUN apk --no-cache add python libsodium-dev
ADD . /shadowsocksr

WORKDIR /shadowsocksr
CMD python server.py