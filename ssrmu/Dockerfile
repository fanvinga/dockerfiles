FROM python:alpine3.7
MAINTAINER FAN VINGA<fanalcest@gmail.com>

ENV DOMAIN=your_domain \
    MUKEY=your_mukey \
    NODEID=3 

RUN  apk --no-cache add --virtual .build-deps \
                        git \
                        tar \          
                        autoconf \
                        automake \
                        make \
                        build-base \
                        linux-headers && \
     apk --no-cache add --virtual runtime-tools \
                        curl \
                        libsodium-dev \
                        openssl-dev \
                        udns-dev \
                        mbedtls-dev \
                        pcre-dev \
                        libev-dev \
                        libtool \
                        libffi-dev && \
     git clone -b manyuser https://github.com/SakuraSa233/shadowsocks.git "/root/shadowsocks" --depth 1 && cd /root/shadowsocks && \
     git checkout 0732973 && \
     pip install --no-cache-dir -r requirements.txt && \
     cp apiconfig.py userapiconfig.py && \
     cp config.json user-config.json && \
     apk del .build-deps

WORKDIR /root/shadowsocks

CMD sed -i "s#https://zhaoj.in#https://${DOMAIN}#" /root/shadowsocks/userapiconfig.py && \
    sed -i "s#glzjin#${MUKEY}#" /root/shadowsocks/userapiconfig.py && \
    sed -i "s#NODE_ID\ =\ 1#NODE_ID\ =\ ${NODEID}#" /root/shadowsocks/userapiconfig.py && \
    python /root/shadowsocks/server.py
