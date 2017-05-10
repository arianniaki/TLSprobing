import requests
from netaddr import IPNetwork
import json
import sys
from OpenSSL import crypto
import ssl
import json
import subprocess
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import OpenSSL
import socket

subnet_file_name = sys.argv[1]
F = open(subnet_file_name,"r")
list_of_subnets = F.readlines()
print(list_of_subnets)
ipnum = 0
for subnet in list_of_subnets:
	for ip in IPNetwork(subnet.replace('\n','')):
		ipnum += 1

print ipnum	
