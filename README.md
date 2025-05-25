SOURCE FROM: https://github.com/tknv/docker-freeradius-eap-ttls

```bash
docker-compose up -d
docker-compose up -build
eapol_test -c ttls-pap.conf -a 127.0.0.1 -p 1812 -s symbol123
```
## WARNING

This is for lab use only. **Not secure at all.**
Better not touch certs directory all.
