FROM alpine:3.18

RUN apk update \
 && apk add --no-cache wpa_supplicant

COPY wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf

CMD ["wpa_supplicant","-c","/etc/wpa_supplicant/wpa_supplicant.conf","-i","eth0","-ddd"]
