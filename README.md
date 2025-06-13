SOURCE FROM: https://github.com/tknv/docker-freeradius-eap-ttls

This helps quick setup EAP TTLS for testing WPA2-Enterprise EAP TTLS. User authentication by ldap (LDAP TLS in TLS tunnel) FreeRadius service it. Configs for v3.0.x. Openldap service via ldaps/ldap. Configs for v1.5.0.

```bash
docker-compose up --build -d
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
