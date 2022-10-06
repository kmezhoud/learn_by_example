FROM nginx:alpine

COPY nginx.conf /etc/nginx/nginx.conf

# Copy private key and certificate of mobi100c.tk
COPY /origin_cert_from_cloudflare/fullshinydomain.ml.crt /etc/ssl/certs/
COPY /origin_cert_from_cloudflare/fullshinydomain.ml.key /etc/ssl/private/