import json
import numpy

from elasticsearch import Elasticsearch
from glob import glob


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


print("------------------------------------------")

university = ["Purdue", "Rice", "Stony Brook", "Stanford" , "final_University of California, Los Angeles_servers", "UCSB", "Yale", "Virginia", "UPenn", "Oregon", "Miami", "Duke", "Colorado", "Berkeley", "USC","Utah", "UW","UTexas"]

ciphersuite_dict = {}


print("_________________")
for uni in university:
		http2_success = 0
		http2_fallbacktohttp11 = 0
		http2_fallbacktohttp1 = 0
		# Initialize the scroll
		page = es.search(
		  index = 'http',
		  doc_type = 'http',
		  scroll = '2m',
		  size = 10000,
		  body = {
			  
		  "query": {
		    "bool": {
		      "must": [
			{ "match": { "university": uni } },
            		{"match" :{ "--http2": "HTTP/2.0"}}

		      ]
		    }
		  }
		    })


		sid = page['_scroll_id']
		scroll_size = page['hits']['total']
		print uni+": " + str(scroll_size)
		print("_____________")
		#for a in page['hits']['hits']:
		#	source = (a['_source'])
		#	if ( source.get('url') not in urls ):
		#		urls.append(source.get('url'))
			#print(urls) 
		print("LEN")
		for i in range(int(scroll_size)):
			#print (page['hits']['hits'][i]['_source']['--http2'])
			if ('HTTP/2.0' in page['hits']['hits'][i]['_source']['--http2']):
				http2_success += 1
			if ('HTTP/1.1' in page['hits']['hits'][i]['_source']['--http2']):
				http2_fallbacktohttp11 +=1
			if ('HTTP/1.0' in page['hits']['hits'][i]['_source']['--http2']):
				http2_fallbacktohttp1 +=1
		print('http2:', http2_success)
		print('fallback http1.1:' , http2_fallbacktohttp11)
		print('fallback http1:' ,http2_fallbacktohttp1)
			
			






		#print("unique urls:"+str(len(urls)))
		#for a in page['hits']['hits']:
		#	source = (a['_source'])
		#	cert_duration.append(int(source.get('certificate_duration')))
		#print(page['hits']['hits'])
		#a = numpy.array(cert_duration)
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

