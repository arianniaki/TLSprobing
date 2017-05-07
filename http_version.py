# http://stackoverflow.com/questions/1210883/determine-supported-http-version-by-the-web-server
from netaddr import IPNetwork
import subprocess
import sys
import json

http_vers = ['--http1.0', '--http1.1', '--http2']

file_to_read = sys.argv[1]
F = open(file_to_read,"r")
list_of_servers = F.readlines()

file_to_read_name, file_to_read_format = file_to_read.split('.')

#f= open("output.txt","w+")

response_json = {}
children = []

for server in list_of_servers:
	url,servername,subnet = server.split(',')
	data = {}
	data['university'] = file_to_read_name
	data['url'] = url
	have_response = False
	#f.write("Url: %s \n" % url)
	for http in http_vers:		
		print '%s' % url
		p = subprocess.Popen(["curl",http,'--head', '-k' ,str(url),'-m','2'], stdout=subprocess.PIPE)
		out, err = p.communicate()
		print('=====ss======')
		print(out)
		print('=====ee======')
		#f.write("\t HTTP versions : %s \n" % http)	
		if out:
			out2 = out.splitlines()	
			data[http] =  out2[0]
			have_response = True	
			#f.write("\t\t %s \n " % out2[0])
	if have_response:
		children.append(data)
response_json["servers"] = children
print json.dumps(response_json,indent=2)
with open(file_to_read_name + '_http.json', 'a') as outfile:
	json.dump(response_json, outfile)

		
#f.close()	
