import sys
import json

from datetime import datetime


subnet_file_name = sys.argv[1]
outlist = []
with open(subnet_file_name, 'r') as of:
	line = of.read()
	print(line)
	f = json.loads(line)
	jsons = f['servers']
	for item in jsons:
		url = json.loads(item)
		outlist.append(url)

response_json = {}
response_json["servers"] = outlist
print ('\n')
print('\n')
a= json.dumps(response_json)

with open(subnet_file_name+'_openssl_fixed.json', 'w') as outfile:
	json.dump(a, outfile)
