FROM alpine:3.7

ENV FRP_VERSION 0.14.1

RUN apk --no-cache add wget 

RUN wget --no-check-certificate https://github.com/fatedier/frp/releases/download/v${FRP_VERSION}/frp_${FRP_VERSION}_linux_amd64.tar.gz && \ 
    tar xzf frp_${FRP_VERSION}_linux_amd64.tar.gz && \
    cd frp_${FRP_VERSION}_linux_amd64 && \
    mv frps /frps && \
    mv frpc /frpc && \
    mv frps.ini /frps.ini && \
    mv frpc.ini /frpc.ini && \
    cd .. && \
    rm -rf *.tar.gz && \
    rm -rf frp_${FRP_VERSION}_linux_amd64 && \
    apk del wget

WORKDIR /
EXPOSE 80 443 6000 7000 7500

ENTRYPOINT ["/frps"]
