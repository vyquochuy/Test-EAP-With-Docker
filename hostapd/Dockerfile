FROM ubuntu:22.04
RUN apt-get update && apt-get install -y hostapd
COPY hostapd.conf /etc/hostapd/hostapd.conf
CMD ["hostapd","-dd","/etc/hostapd/hostapd.conf"]
