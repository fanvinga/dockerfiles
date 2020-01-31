FROM alpine:3
MAINTAINER FAN VINGA<fanalcest@gmail.com>
MAINTAINER WU DYLAN<nextdoorwu@gmail.com>

ENV BROOK_VER=20200201 \
    MODE=server \
    PASSWORD=hyperapp \
    PORT=8888

RUN wget --no-check-certificate https://github.com/txthinking/brook/releases/download/v${BROOK_VER}/brook && \
    chmod +x brook

WORKDIR /
EXPOSE ${PORT}

CMD /brook ${MODE} -l :${PORT} -p ${PASSWORD}
