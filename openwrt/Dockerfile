FROM debian:latest as builder

SHELL ["/bin/bash", "-c"]

ENV FORCE_UNSAFE_CONFIGURE=1 \
        PROFILE="xiaoyu_xy-c5" \
        SDK="openwrt-sdk-ramips-mt7621_gcc-8.4.0_musl.Linux-x86_64" \
        IMAGEBUILDER="openwrt-imagebuilder-ramips-mt7621.Linux-x86_64" \
        PREFIX="https://downloads.openwrt.org/snapshots/targets/ramips/mt7621" \
        PACKAGES="vim htop wget bind-dig libustream-openssl ca-certificates luci luci-i18n-base-zh-cn \
                                avahi-utils netatalk shadow e2fsprogs fdisk lsblk block-mount luci-app-hd-idle luci-app-mwan3 \
                                automount autosamba minieap luci-proto-minieap \
                                -ppp -ppp-mod-pppoe -ip6tables -odhcp6c -kmod-ipv6 -kmod-ip6tables -luci-proto-ipv6 -odhcpd-ipv6only"

COPY . /tmp/

RUN apt update && apt install -y build-essential libncurses5-dev libncursesw5-dev zlib1g-dev gawk git gettext libssl-dev xsltproc wget curl unzip python3
    
RUN curl -fsSL ${PREFIX}/${IMAGEBUILDER}.tar.xz | tar -xJ && cd ${IMAGEBUILDER} && cp /tmp/*.ipk packages/ \
    && make image CONFIG_IPV6=n PROFILE=${PROFILE} PACKAGES="${PACKAGES}" BIN_DIR=/root

FROM alpine as prod

RUN apk add --no-cache python3
COPY --from=builder /root /root

CMD python3 -m http.server -d ~ 80
