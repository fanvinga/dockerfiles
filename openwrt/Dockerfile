FROM debian:latest as builder

SHELL ["/bin/bash", "-c"]

ENV FORCE_UNSAFE_CONFIGURE=1 \
    PROFILE="xiaoyu_xy-c5"   \
    SDK="openwrt-sdk-ramips-mt7621_gcc-8.3.0_musl.Linux-x86_64"                          \
    IMAGEBUILDER="openwrt-imagebuilder-ramips-mt7621.Linux-x86_64"                       \
    PREFIX="https://downloads.openwrt.org/snapshots/targets/ramips/mt7621"               \
    PACKAGES="vim htop wget bind-dig libustream-openssl ca-certificates luci luci-i18n-base-zh-cn   \
              avahi-utils netatalk shadow-groupadd shadow-groupdel shadow-useradd shadow-userdel    \
              automount autosamba e2fsprogs fdisk lsblk block-mount luci-app-hd-idle luci-app-mwan3 \
              minieap luci-proto-minieap \
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

RUN curl -fsSL ${PREFIX}/${SDK}.tar.xz | tar -xJ && cd ${SDK} \
    && svn checkout https://github.com/coolsnowwolf/lede/trunk/package/lean/automount package/automount  \
    && svn checkout https://github.com/coolsnowwolf/lede/trunk/package/lean/autosamba package/autosamba  \
    && git clone --depth 1 https://github.com/fanvinga/openwrt-minieap.git package/minieap               \
    && make PROFILE=${PROFILE} defconfig && make package/{automount,autosamba,minieap}/compile 

ADD https://github.com/ysc3839/luci-proto-minieap/releases/download/v2.0-0/luci-proto-minieap_2.0-1_all.ipk /${SDK}/bin/packages/mipsel_24kc/base/
    
RUN curl -fsSL ${PREFIX}/${IMAGEBUILDER}.tar.xz | tar -xJ && cd ${IMAGEBUILDER} \
    && cp /${SDK}/bin/packages/mipsel_24kc/base/*.ipk packages/ \
    && make image CONFIG_IPV6=n PROFILE=${PROFILE} PACKAGES="${PACKAGES}" BIN_DIR=/root

FROM alpine as prod

RUN apk add --no-cache python3
COPY --from=builder /root /root

CMD python3 -m http.server -d ~ 80
