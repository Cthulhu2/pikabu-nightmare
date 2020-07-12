# pikabu-nightmare

## Architecture

[architecture](docs/architecture.puml)

Visit [WillBooster/plantuml-visualizer](https://github.com/WillBooster/plantuml-visualizer)

## Docker 

To build and launch containers in docker network in project dir run: 
```
docker-compose -f ./docker-compose-dev.yml up -d
```
Published `nginx` ports are accessible by `http://localhost`.

`registrator` will (de)register a service node in `consul` for each container
automagically.
`nginx.conf` be re-created from template and reloaded on each node registration. 

To find `consul` IP-address, see in `portainer` or use command:
```
$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' consul
```
So, for example, `consul` UI url be `http://172.25.0.2:8500/ui`,
 
Also, all registered and healthy services be presented in `consul` DNS
server in `pn.local` domain, `dc1` datacenter.
```
$ dig @172.25.0.2 nginx-http.service.dc1.pn.local ANY
...
;; ANSWER SECTION:
nginx-http.service.dc1.pn.local. 0 IN	A	172.25.0.3
```

Visit:
* [Install Docker Engine](https://docs.docker.com/engine/install/)
* [Install Docker Compose](https://docs.docker.com/compose/install/)
* [Compose file version 3 reference](https://docs.docker.com/compose/compose-file/)
* https://www.portainer.io/
* [Consul DNS Interface](https://www.consul.io/docs/agent/dns.html)
