FROM python:alpine3.7
MAINTAINER FAN VINGA<fanalcest@gmail.com>

ENV NODE_ID=1                     \
    SPEEDTEST=6                   \
    CLOUDSAFE=1                   \
    AUTOEXEC=0                    \
    ANTISSATTACK=0                \
    MU_SUFFIX=zhaoj.in            \
    MU_REGEX=%5m%id.%suffix       \
    API_INTERFACE=modwebapi       \
    WEBAPI_URL=https://zhaoj.in   \
    WEBAPI_TOKEN=glzjin           \
    MYSQL_HOST=127.0.0.1          \
    MYSQL_USER=ss                 \
    MYSQL_PASS=ss                 \
    MYSQL_DB=shadowsocks          \
    REDIRECT=github.com           \
    FAST_OPEN=false

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
     git clone -b manyuser https://github.com/glzjin/shadowsocks.git "/root/shadowsocks" --depth 1 && \
     cd  /root/shadowsocks                    && \
     pip install -r requirements.txt          && \
     cp  apiconfig.py userapiconfig.py        && \
     cp  config.json  user-config.json        && \
     apk del .build-deps && touch /etc/hosts.deny

WORKDIR /root/shadowsocks

CMD sed -i "s|NODE_ID = 1|NODE_ID = ${NODE_ID}|"                               /root/shadowsocks/userapiconfig.py && \
    sed -i "s|SPEEDTEST = 6|SPEEDTEST = ${SPEEDTEST}|"                         /root/shadowsocks/userapiconfig.py && \
    sed -i "s|CLOUDSAFE = 1|CLOUDSAFE = ${CLOUDSAFE}|"                         /root/shadowsocks/userapiconfig.py && \
    sed -i "s|AUTOEXEC = 0|AUTOEXEC = ${AUTOEXEC}|"                            /root/shadowsocks/userapiconfig.py && \
    sed -i "s|ANTISSATTACK = 0|ANTISSATTACK = ${ANTISSATTACK}|"                /root/shadowsocks/userapiconfig.py && \
    sed -i "s|MU_SUFFIX = 'zhaoj.in'|MU_SUFFIX = '${MU_SUFFIX}'|"              /root/shadowsocks/userapiconfig.py && \
    sed -i "s|MU_REGEX = '%5m%id.%suffix'|MU_REGEX = '${MU_REGEX}'|"           /root/shadowsocks/userapiconfig.py && \
    sed -i "s|API_INTERFACE = 'modwebapi'|API_INTERFACE = '${API_INTERFACE}'|" /root/shadowsocks/userapiconfig.py && \
    sed -i "s|WEBAPI_URL = 'https://zhaoj.in'|WEBAPI_URL = '${WEBAPI_URL}'|"   /root/shadowsocks/userapiconfig.py && \
    sed -i "s|MWEBAPI_TOKEN = 'glzjin'|WEBAPI_TOKEN = '${WEBAPI_TOKEN}'|"      /root/shadowsocks/userapiconfig.py && \
    sed -i "s|MYSQL_HOST = '127.0.0.1'|MYSQL_HOST = '${MYSQL_HOST}'|"          /root/shadowsocks/userapiconfig.py && \
    sed -i "s|MYSQL_USER = 'ss'|MYSQL_USER = '${MYSQL_USER}'|"                 /root/shadowsocks/userapiconfig.py && \
    sed -i "s|MYSQL_PASS = 'ss'|MYSQL_PASS = '${MYSQL_PASS}'|"                 /root/shadowsocks/userapiconfig.py && \
    sed -i "s|MYSQL_DB = 'shadowsocks'|MYSQL_DB = '${MYSQL_DB}'|"              /root/shadowsocks/userapiconfig.py && \
    sed -i "s|\"redirect\": \"\"|\"redirect\": \"${REDIRECT}\"|"               /root/shadowsocks/user-config.json && \
    sed -i "s|\"fast_open\": false|\"fast_open\": ${FAST_OPEN}|"               /root/shadowsocks/user-config.json && \
    python /root/shadowsocks/server.py
