FROM ubuntu:14.04

RUN apt-get update && \
    apt-get install -y python-twisted-web && \
    apt-get autoremove && \
    apt-get clean

RUN mkdir -p /opt/twisted /var/run/twisted

ADD vhoster.rpy /opt/twisted/vhoster.rpy

EXPOSE 8080
WORKDIR /var/run/twisted
CMD twistd -n web --resource /opt/twisted/vhoster.rpy
