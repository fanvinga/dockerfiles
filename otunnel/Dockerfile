FROM alpine:3.8
MAINTAINER FAN VINGA<fanalcest@gmail.com>

ENV BIND_PORT=10000 \
    TOKEN=token

ADD otunnel /
CMD chmod +x /otunnel && \
    /otunnel \
    listen :${BIND_PORT} \
    -s ${TOKEN}
