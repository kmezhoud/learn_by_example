#docker network create sp-example-net
#docker build . -t saml-shinyproxy-mobi100c
#docker run -d -v /var/run/docker.sock:/var/run/docker.sock --net sp-example-net -p 8080:8080 fullShinyDomain

FROM openanalytics/shinyproxy:2.6.1

COPY application.yml /opt/shinyproxy/application.yml

WORKDIR /opt/shinyproxy/
CMD ["java", "-jar", "/opt/shinyproxy/shinyproxy.jar"]