FROM alpine:3.8
MAINTAINER FAN VINGA<fanalcest@gmail.com>

RUN apk --no-cache add git python3 py3-pip && \
    pip3 install flask gunicorn            && \
    git clone --depth 1 https://github.com/rwv/chinese-dos-games /app && \
    cd app && python3 download_data.py     && \
    apk del git && rm -rf /app/.git

WORKDIR /app
EXPOSE 80

CMD gunicorn -w 5 -b 0.0.0.0:80 app:app