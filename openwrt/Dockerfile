FROM debian:latest as builder

SHELL ["/bin/bash", "-c"]
ENV FORCE_UNSAFE_CONFIGURE=1 \
    ARCH="mt7621"            \
    PROFILE="xiaoyu_xy-c5"   \
    PREFIX="https://downloads.openwrt.org/snapshots/targets/ramips/mt7621"               \
    PACKAGES="vim htop wget libustream-openssl ca-certificates luci luci-i18n-base-zh-cn \
             automount autosamba minieap luci-proto-minieap                              \
             e2fsprogs fdisk lsblk usbutils block-mount luci-app-mwan3 luci-app-upnp luci-app-hd-idle \
             avahi-utils netatalk shadow-groupadd shadow-groupdel shadow-useradd shadow-userdel \
             -ppp -ppp-mod-pppoe -ip6tables -odhcp6c -kmod-ipv6 -kmod-ip6tables -luci-proto-ipv6 -odhcpd-ipv6only -kmod-ipt-offload"

RUN apt update && apt install -y build-essential \
                                 curl \
                                 file \
                                 gawk \
                                 gettext \
                                 git \
                                 libncurses5-dev \
                                 libssl-dev \
                                 python2.7 \
                                 python3 \
                                 rsync \
                                 subversion \
                                 sudo \
                                 swig \
                                 unzip \
                                 wget \
                                 zlib1g-dev 

RUN curl -fsSL ${PREFIX}/openwrt-sdk-ramips-${ARCH}_gcc-8.3.0_musl.Linux-x86_64.tar.xz | tar -xJ \
    && mv openwrt-sdk-ramips-${ARCH}_gcc-8.3.0_musl.Linux-x86_64 sdk && cd sdk                           \
    && svn checkout https://github.com/coolsnowwolf/lede/trunk/package/lean/automount package/automount  \
    && svn checkout https://github.com/coolsnowwolf/lede/trunk/package/lean/autosamba package/autosamba  \
    && git clone --depth 1 https://github.com/fanvinga/openwrt-minieap.git package/minieap               \
    && make PROFILE=${PROFILE} defconfig && make package/{automount,autosamba,minieap}/compile 

ADD https://github.com/ysc3839/luci-proto-minieap/releases/download/v2.0-0/luci-proto-minieap_2.0-1_all.ipk /sdk/bin/packages/mipsel_24kc/base/
    
RUN curl -fsSL ${PREFIX}/openwrt-imagebuilder-ramips-${ARCH}.Linux-x86_64.tar.xz | tar -xJ \
    && mv openwrt-imagebuilder-ramips-${ARCH}.Linux-x86_64 imagebuilder && cd imagebuilder \
    && cp /sdk/bin/packages/mipsel_24kc/base/*.ipk packages/ \
    && make image CONFIG_IPV6=n PROFILE=${PROFILE} PACKAGES="${PACKAGES}" BIN_DIR=/root

FROM alpine as prod

RUN apk add --no-cache python3
COPY --from=builder /root /root

CMD python3 -m http.server -d ~ 80
