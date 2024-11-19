# /nginx-reverse-proxy/certbot/Dockerfile
FROM certbot/certbot:v2.5.0

# Install Certbot Nginx Plugin
RUN apk update && \
    apk add --no-cache certbot-nginx

