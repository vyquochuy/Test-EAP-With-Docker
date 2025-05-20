BUILD
    docker build -t local/hostapd ./hostapd
    docker build -t local/supplicant ./supplicant

Bootstrap chứng chỉ EAP-TLS trong container

    Khởi động freeradius:
        docker-compose up -d freeradius

    Vào container và khởi tạo certs:
        docker exec -it freeradius bash -c \
            "cd /etc/freeradius/3.0/certs && ./bootstrap"

    Copy ra host:
        docker cp freeradius:/etc/freeradius/3.0/certs radius-config/

    Tắt container freeradius:
        docker-compose down

Khởi động toàn bộ và test
    docker-compose up --build
