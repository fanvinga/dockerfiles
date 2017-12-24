FROM python:2.7.14-alpine3.6
MAINTAINER FAN VINGA<fanalcest@gmail.com>

ADD . /usr/app

RUN  apk --update --no-cache add --virtual .build-deps \
                        git \
                        tar \          
                        autoconf \
                        automake \
                        make \
                        build-base \
                        linux-headers && \
     apk add --virtual runtime-tools \                       
                        openssl-dev \
                        libffi-dev && \                                  
     mkdir -p /usr/app/db && \
     pip install requests[security] && \
     pip install -r /usr/app/requirements.txt && \
     apk del .build-deps && rm -rf /var/cache/apk/*

WORKDIR "/usr/app/db"
ENTRYPOINT ["python"]
CMD ["/usr/app/main.py"]