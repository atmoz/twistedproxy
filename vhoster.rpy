# Got this awesome code from Jean-Paul Calderone <exarkun@twistedmatrix.com>

from os import environ
from pprint import pprint

from twisted.web.vhost import NameVirtualHost
from twisted.web.proxy import ReverseProxyResource
from twisted.web.server import Site

root = NameVirtualHost()

pprint(environ)

for k, v in environ.items():
    if k.startswith(b"PROXY_") and k.endswith(b"ADDR"):
       parts = k.split(b"_")
       host = parts[1].lower()
       address = v
       port = int(environ[k[:-len(b"ADDR")] + b"PORT"])

       print 'Adding virtual', host, 'proxying to', repr(address), repr(port)

       root.addHost(host, ReverseProxyResource(address, port, b""))

print 'Finished adding virtual hosts'

resource = Site(root)
