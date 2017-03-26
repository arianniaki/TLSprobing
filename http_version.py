# http://stackoverflow.com/questions/1210883/determine-supported-http-version-by-the-web-server
from netaddr import IPNetwork
import subprocess



for ip in IPNetwork('130.245.0.0/16'):
	print '%s' % ip
	p = subprocess.Popen(["curl",'--http1.1','--head' ,str(ip),'-m','1'], stdout=subprocess.PIPE)
	out, err = p.communicate()
#print out
	print(out)
