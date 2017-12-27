FROM python:2-alpine3.7
MAINTAINER FAN VINGA<fanalcest@gmail.com>

ADD . /usr/app

RUN  apk --no-cache add --virtual .build-deps \
                        git \
                        tar \          
                        autoconf \
                        automake \
                        make \
                        build-base \
                        linux-headers && \
     apk --no-cache add --virtual runtime-tools \                       
                        openssl-dev \
                        libffi-dev && \                                  
     mkdir -p /usr/app/db && \
     pip install requests[security] && \
     pip install -r /usr/app/requirements.txt && \
     apk del .build-deps

WORKDIR "/usr/app/db"
ENTRYPOINT ["python"]
CMD ["/usr/app/main.py"]