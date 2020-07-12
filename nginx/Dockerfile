FROM nginx:1.19.0-alpine

# Nginx with consul-template service
# to dynamically re-create and reload nginx.conf based on consul service config

ENV CT_URL https://releases.hashicorp.com/consul-template/0.25.0/consul-template_0.25.0_linux_amd64.tgz
ENV CONSUL_ADDR consul:8500
COPY consul-template.service /etc/service/consul-template/run
COPY nginx.service /etc/service/nginx/run
COPY nginx.ctmpl /etc/consul-templates/nginx.ctmpl

RUN apk --update --no-cache add runit \
  && curl -L $CT_URL | tar -C /usr/local/bin -zxf - \
  && chmod a+x /etc/service/nginx/run \
  && chmod a+x /etc/service/consul-template/run \
  && rm -v /etc/nginx/conf.d/*

CMD ["runsvdir", "/etc/service"]
