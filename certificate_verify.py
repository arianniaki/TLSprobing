import requests
from netaddr import IPNetwork
import json

def check_ssl(url):
    try:
        req = requests.get(url, verify=True,timeout=0.1)
        print url + ' has a valid SSL certificate!'
        print req.headers
    except requests.exceptions.SSLError:
        print url + ' has INVALID SSL certificate!'
    except requests.exceptions.ConnectionError:
    	print url + ' Not SSL'
    	newurl = url.replace("https","http")
    	print(newurl)
    	try:
    		req = requests.get(newurl,timeout = 0.1)
    		print req.headers
    		print('------')
    	except requests.exceptions.ConnectionError:
    		print("Not a Web Server")
    	except requests.exceptions.ReadTimeout:
    		print ("timeout No web server at all")
    except requests.exceptions.ReadTimeout:
    	print 'timeout'

check_ssl('https://google.com')
check_ssl('https://example.com')
check_ssl('https://netsys.cs.stonybrook.edu')
check_ssl('https://130.245.1.103')
for ip in IPNetwork('130.245.0.0/16'):
	print '%s' % ip
	check_ssl('https://'+str(ip))