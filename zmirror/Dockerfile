FROM alpine:3.8
MAINTAINER FAN VINGA<fanalcest@gmail.com>

ENV GOAL=google_and_zhwikipedia \
    FUNC=youtube                \
    DOMAIN=vinga.tech

RUN apk --no-cache add gcc g++ git python3 python3-dev libc-dev                            && \
    pip3 install --upgrade --no-cache-dir pip                                              && \
    pip3 install --no-cache-dir gunicorn gevent requests flask cchardet fastcache lru-dict && \
    git clone https://github.com/aploium/zmirror /app --depth 1                            && \
    apk del --purge gcc g++ git libc-dev && rm -rf /src /app/.git

WORKDIR /app
EXPOSE  80

CMD cp more_configs/config_${GOAL}.py config.py           && \
    cp more_configs/custom_func_${FUNC}.py custom_func.py && \
    sed -i "/my_host_name/d" config.py                    && \
    echo "my_host_name = '${DOMAIN}'" >> config.py        && \
    gunicorn --bind 0.0.0.0:80 --workers 8 --worker-connections 1000 wsgi:application