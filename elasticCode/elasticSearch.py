import json
import numpy

from elasticsearch import Elasticsearch
from glob import glob


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


print("------------------------------------------")

ciphers = ['ECDHE-RSA-AES256-GCM-SHA384','ECDHE-ECDSA-AES256-GCM-SHA384','ECDHE-RSA-AES256-SHA384','ECDHE-ECDSA-AES256-SHA384','ECDHE-RSA-AES256-SHA','ECDHE-ECDSA-AES256-SHA','SRP-DSS-AES-256-CBC-SHA','SRP-RSA-AES-256-CBC-SHA','SRP-AES-256-CBC-SHA','DH-DSS-AES256-GCM-SHA384','DHE-DSS-AES256-GCM-SHA384','DH-RSA-AES256-GCM-SHA384','DHE-RSA-AES256-GCM-SHA384','DHE-RSA-AES256-SHA256','DHE-DSS-AES256-SHA256','DH-RSA-AES256-SHA256','DH-DSS-AES256-SHA256','DHE-RSA-AES256-SHA','DHE-DSS-AES256-SHA','DH-RSA-AES256-SHA','DH-DSS-AES256-SHA','DHE-RSA-CAMELLIA256-SHA','DHE-DSS-CAMELLIA256-SHA','DH-RSA-CAMELLIA256-SHA','DH-DSS-CAMELLIA256-SHA','ECDH-RSA-AES256-GCM-SHA384','ECDH-ECDSA-AES256-GCM-SHA384','ECDH-RSA-AES256-SHA384','ECDH-ECDSA-AES256-SHA384','ECDH-RSA-AES256-SHA','ECDH-ECDSA-AES256-SHA','AES256-GCM-SHA384','AES256-SHA256','AES256-SHA','CAMELLIA256-SHA','PSK-AES256-CBC-SHA','ECDHE-RSA-AES128-GCM-SHA256','ECDHE-ECDSA-AES128-GCM-SHA256','ECDHE-RSA-AES128-SHA256','ECDHE-ECDSA-AES128-SHA256','ECDHE-RSA-AES128-SHA','ECDHE-ECDSA-AES128-SHA','SRP-DSS-AES-128-CBC-SHA','SRP-RSA-AES-128-CBC-SHA','SRP-AES-128-CBC-SHA','DH-DSS-AES128-GCM-SHA256','DHE-DSS-AES128-GCM-SHA256','DH-RSA-AES128-GCM-SHA256','DHE-RSA-AES128-GCM-SHA256','DHE-RSA-AES128-SHA256','DHE-DSS-AES128-SHA256','DH-RSA-AES128-SHA256','DH-DSS-AES128-SHA256','DHE-RSA-AES128-SHA','DHE-DSS-AES128-SHA','DH-RSA-AES128-SHA','DH-DSS-AES128-SHA','DHE-RSA-SEED-SHA','DHE-DSS-SEED-SHA','DH-RSA-SEED-SHA','DH-DSS-SEED-SHA','DHE-RSA-CAMELLIA128-SHA','DHE-DSS-CAMELLIA128-SHA','DH-RSA-CAMELLIA128-SHA','DH-DSS-CAMELLIA128-SHA','ECDH-RSA-AES128-GCM-SHA256','ECDH-ECDSA-AES128-GCM-SHA256','ECDH-RSA-AES128-SHA256','ECDH-ECDSA-AES128-SHA256','ECDH-RSA-AES128-SHA','ECDH-ECDSA-AES128-SHA','AES128-GCM-SHA256','AES128-SHA256','AES128-SHA','SEED-SHA','CAMELLIA128-SHA','PSK-AES128-CBC-SHA','ECDHE-RSA-RC4-SHA','ECDHE-ECDSA-RC4-SHA','ECDH-RSA-RC4-SHA','ECDH-ECDSA-RC4-SHA','RC4-SHA','RC4-MD5','PSK-RC4-SHA','ECDHE-RSA-DES-CBC3-SHA','ECDHE-ECDSA-DES-CBC3-SHA','SRP-DSS-3DES-EDE-CBC-SHA','SRP-RSA-3DES-EDE-CBC-SHA','SRP-3DES-EDE-CBC-SHA','EDH-RSA-DES-CBC3-SHA','EDH-DSS-DES-CBC3-SHA','DH-RSA-DES-CBC3-SHA','DH-DSS-DES-CBC3-SHA','ECDH-RSA-DES-CBC3-SHA','ECDH-ECDSA-DES-CBC3-SHA','DES-CBC3-SHA','PSK-3DES-EDE-CBC-SHA']


university = ["Purdue", "Rice", "Stony Brook", "Stanford" , "UCLA", "UCSB", "Yale", "Virginia", "UPenn", "Oregon", "Miami", "Duke", "Colorado", "Berkeley", "USC","Utah", "UW","UTexas"]


for uni in university:
	urls = []
	cert_duration = []
	# Initialize the scroll
	page = es.search(
	  index = 'openssls',
	  doc_type = 'openssl',
	  scroll = '2m',
	  size = 10000,
	  body = {
		  
	  "query": {
	    "bool": {
	      "must": [
		{ "match": { "university": uni } },


	      ]
	    }
	  }
	    })


	sid = page['_scroll_id']
	scroll_size = page['hits']['total']
	print uni+": " + str(scroll_size)
	print("_____________")

	#print page['hits']['hits']
	for a in page['hits']['hits']:
		source = (a['_source'])
		if ( source.get('url') not in urls ):
			urls.append(source.get('url'))
		#print(urls) 
		#print("unique urls:"+str(len(urls)))
	print("LEN url ",len(urls))


	#for a in page['hits']['hits']:
	#	source = (a['_source'])
	#	cert_duration.append(int(source.get('certificate_duration')))
	#	a = numpy.array(cert_duration)
	#print(numpy.average(a))

	while (scroll_size > 0):
		print "Scrolling..."
		page = es.scroll(scroll_id = sid, scroll = '2m')
		# Update the scroll ID
		sid = page['_scroll_id']
		# Get the number of results that we returned in the last scroll
		scroll_size = len(page['hits']['hits'])
		print "scroll size: " + str(scroll_size)
		print(len(page['hits']['hits']), "page hits")
		#for a in page['hits']['hits']:
		#	print(a)
		#	print('\n')
		print(len(page['hits']['hits']))

