SOURCE FROM: https://github.com/tknv/docker-freeradius-eap-ttls

```bash
docker-compose up --build
docker-compose up 
eapol_test -c ttls-pap.conf -s symbol123
```

if error "Attaching to openldap, phpldapadmin, radius-eap-ttls
Error response from daemon: ... 
failed to bind host port for 0.0.0.0:1812:172.22.0.3:1812/udp: address already in use"

```bash
sudo ss -tulnp | grep 1812
sudo kill <ip_address>
```


## WARNING

This is for lab use only. **Not secure at all.**
Better not touch certs directory all.
