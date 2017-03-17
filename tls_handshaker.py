#https://github.com/tintinweb/scapy-ssl_tls
import scapy
from scapy.layers.ssl_tls import *
import socket

target = ('130.245.27.2',443)

# create tcp socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# connect socket to target
s.connect(target)
# create a TLSRecord using Scapy and set the version to SSL_3_0
p = TLSRecord(version="SSL_3_0")/TLSHandshake()/TLSClientHello(version="SSL_3_0")
# send the TLSRecord on the socket
s.sendall(str(p))
# receive the sockets response
resp = s.recv(8192)
print "resp: %s"%repr(resp)
s.close()