FROM alpine:latest
MAINTAINER FAN VINGA<fanalcest@gmail.com>
MAINTAINER WU DYLAN<nextdoorwu@gmail.com>

ENV BROOK_VER=20171113 \
    MODE=server \
    PASSWORD=hyperapp \
    PORT=8888

RUN apk --update --no-cache add wget && \
    wget --no-check-certificate https://github.com/txthinking/brook/releases/download/v${BROOK_VER}/brook && \
    chmod +x brook && \
    apk del wget && \
    rm -rf /var/cache/apk/*

WORKDIR /
EXPOSE ${PORT}

CMD /brook ${MODE} -l :${PORT} -p ${PASSWORD}
