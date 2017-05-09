import json
from elasticsearch import Elasticsearch
from glob import glob

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


print("------------------------------------------")

# Initialize the scroll
page = es.search(
  index = 'networksproject_curl',
  doc_type = 'certificates',
  size = 1000,
  body = {
	  
  "query": {
    "bool": {
      "must": [
        { "match": { "university": "Purdue" } },
#         { "match": { "has_expired": "True" } }
      ]
    }
  }
	  
	
    })


for a in page['hits']['hits']:
	print(a)
	print('\n')
print(len(page['hits']['hits']))
