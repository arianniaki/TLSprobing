import sys
import json

from datetime import datetime

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)


subnet_file_name = sys.argv[1]
outlist = []
with open(subnet_file_name, 'r') as of:
	f = json.loads(of.read())
	jsons = f['certificates']
	for item in jsons:
		url = json.loads(item)
		url['certificate_duration'] = str(days_between(url['not_after'],url['not_before']))
		outlist.append(url)

response_json = {}
response_json["certificates"] = outlist
print ('\n')
print('\n')
a= json.dumps(response_json)

with open(subnet_file_name+'_cert_duration.json', 'w') as outfile:
	json.dump(a, outfile)
