twistedproxy
============

Proxy for Docker containers using Twisted

## Usage

`docker build --tag twistedproxy .`

`docker run -d --link some_container_name:PROXY_example.com twistedproxy`
