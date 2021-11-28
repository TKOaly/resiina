FROM frappe/frappe-worker:version-13 AS worker

RUN echo 'frappe' > /home/frappe/frappe-bench/sites/apps.txt

FROM frappe/frappe-nginx:version-13 AS nginx

COPY --from=worker /home/frappe/frappe-bench/sites/ /var/www/html/
RUN echo 'Hello, CI!' > /var/www/html/assets/hello-ci.txt

VOLUME ["/assets"]
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
