FROM frappe/frappe-worker:version-13 AS worker

RUN install_app resiina https://github.com/TKOaly/resiina

FROM bitnami/node:12-prod AS temp

RUN apt-get update && apt-get install -y git

COPY install_app.sh install_app
RUN ./install_app resiina https://github.com/TKOaly/resiina main version-13

FROM frappe/frappe-nginx:version-13 AS nginx

COPY --from=temp /home/frappe/frappe-bench/sites/ /var/www/html/
COPY --from=temp /rsync /rsync
RUN echo 'resiina' >> /var/www/html/apps.txt

VOLUME ["/assets"]
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
