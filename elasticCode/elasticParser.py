import json
from elasticsearch import Elasticsearch
from glob import glob

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

outlist = []
for infile in glob('json_bank_openssl/*'):
    with open(infile, 'r') as of:
    	print(infile)
        f = json.loads(of.read())
        outlist += f['servers']
        #outlist += f['servers']
print len(outlist)

    
i = 0
for item in outlist:
    i=i+1
    es.index(index='openssls', doc_type='openssl', id=i, body=json.loads(item))
    
