FROM alpine:latest
MAINTAINER FAN VINGA<fanalcest@gmail.com>

ENV BIND_PORT=10000 \
    TOKEN=otunnel

ADD otunnel /
CMD chmod +x /otunnel && \
    /otunnel \
    listen :${BIND_PORT} \
    -s ${TOKEN}
