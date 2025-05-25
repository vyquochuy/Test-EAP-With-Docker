FROM ubuntu:24.04

RUN apt update && apt install -y \
    git \
    wget \
    libssl-dev \
    pkg-config \
    libnl-3-dev \
    libdbus-1-dev \
    build-essential \
    ca-certificates \
    libnl-genl-3-dev \
    libnl-route-3-dev \
    && rm -rf /var/lib/apt/lists/*

# Tải release tarball (ví dụ version 2.10)
RUN wget https://w1.fi/releases/wpa_supplicant-2.10.tar.gz -O /tmp/wpa_supplicant.tar.gz \
    && tar xzf /tmp/wpa_supplicant.tar.gz -C /opt/ \
    && mv /opt/wpa_supplicant-2.10 /opt/wpa_supplicant

WORKDIR /opt/wpa_supplicant/wpa_supplicant

# Bật EAP-DPSK, tắt D-Bus ctrl_iface
RUN cp defconfig .config && \
    echo "CONFIG_EAP_GPSK=y"        >> .config && \
    echo "CONFIG_CTRL_IFACE_DBUS=n" >> .config && \
    cat .config 

# Build eapol_test
RUN make eapol_test -j$(nproc)

# Copy binary sang image mới
FROM ubuntu:24.04

COPY --from=0 /opt/wpa_supplicant/wpa_supplicant/eapol_test /usr/local/bin/

# Thêm runtime dependencies
RUN apt update && apt install -y \
    ca-certificates \
    libdbus-1-3 \
    libnl-3-200 \
    libnl-genl-3-200 \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/usr/local/bin/eapol_test"]