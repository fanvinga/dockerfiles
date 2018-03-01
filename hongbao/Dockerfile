FROM alpine:3.7
MAINTAINER FAN VINGA<fanalcest@gmail.com>

RUN apk --no-cache add git nodejs nodejs-npm && \
    git clone https://github.com/game-helper/hongbao --depth 1   && \
    cd /hongbao/web && \
    npm install     && \
    apk del git 

WORKDIR /hongbao/web

CMD npm run dev