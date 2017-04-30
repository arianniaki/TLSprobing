# http://stackoverflow.com/questions/1210883/determine-supported-http-version-by-the-web-server
from netaddr import IPNetwork
import subprocess
import sys

http_vers = ['--http1.0', '--http1.1', '--http2']

file_to_read = sys.argv[1]
F = open(file_to_read,"r")
list_of_servers = F.readlines()

file_to_read_name, file_to_read_format = file_to_read.split('.')

f= open("output.txt","w+")

for server in list_of_servers:
	url,servername,subnet = server.split(',')
	f.write("Url: %s \n" % url)
	for http in http_vers:		
		print '%s' % url
		p = subprocess.Popen(["curl",http,'--head', '-k' ,str(url),'-m','2'], stdout=subprocess.PIPE)
		out, err = p.communicate()
		print('=====ss======')
		print(out)
		print('=====ee======')
		f.write("\t HTTP versions : %s \n" % http)	
		if out:
			out2 = out.splitlines()		
			f.write("\t\t %s \n " % out2[0])
		
f.close()	
