FROM alpine:latest
MAINTAINER FAN VINGA<fanalcest@gmail.com>

RUN apk --update --no-cache add nginx git && \
    git clone https://github.com/gabrielecirulli/2048 --depth 1 && \
    apk del git && \
    rm -rf /var/cache/apk/* /2048/.git

COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80

CMD ["nginx"]
