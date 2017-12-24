FROM alpine:latest
MAINTAINER FAN VINGA<fanalcest@gmail.com>

ENV GOAL google_and_zhwikipedia
ENV DOMAIN vinga.fun

RUN apk --update --no-cache add gcc g++ git python3 python3-dev && \
    apk add libc-dev && pip3 install --upgrade --no-cache-dir pip && \
    pip3 install --no-cache-dir gunicorn gevent requests flask cchardet fastcache lru-dict 
    
RUN git clone -b v0.30-dev https://github.com/aploium/zmirror /zmirror && cd zmirror --depth 1 && \
    apk del gcc g++ git libc-dev && \
    rm -rf /src && \
    rm -rf /var/cache/apk/*
    
WORKDIR /zmirror
EXPOSE  80

CMD cp more_configs/config_${GOAL}.py config.py && \
    sed -i "s/\'127.0.0.1\'/\'tmp_replace\'/g" config.py && \
    sed -i "s/tmp_replace/${DOMAIN}/g" config.py && \
    gunicorn --bind 0.0.0.0:80 --workers 2 --worker-connections 100 wsgi:application

