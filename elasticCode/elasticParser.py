import json
from elasticsearch import Elasticsearch
from glob import glob

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

outlist = []
for infile in glob('json_bank/*'):
    with open(infile, 'r') as of:
        f = json.loads(of.read())
        outlist += f['certificates']
        #outlist += f['servers']
print len(outlist)

    
i = 0
for item in outlist:
    i=i+1
    es.index(index='networks5', doc_type='certificates', id=i, body=json.loads(item))
    
