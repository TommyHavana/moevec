FROM alpine:3.20
COPY deploy/init-secrets.sh /usr/local/bin/init-secrets
RUN chmod +x /usr/local/bin/init-secrets
ENTRYPOINT ["init-secrets"]
