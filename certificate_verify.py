import requests
from netaddr import IPNetwork
import json
import sys
from OpenSSL import crypto
import ssl
import json


def check_ssl(url,file ):
	if(url != 'https://129.49.4.10'):

		try:
			req = requests.get(url, verify=True,timeout=0.1)
			print url + ' has a valid SSL certificate!'
			ssl_servers_file.write(url+'\n')
			url_without_https = url.replace("https://","")
			cert = ssl.get_server_certificate((url_without_https, 443))
			load_cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
			get_certificate_info(load_cert,url)
			get_curl_info(url,req.headers)

		except requests.exceptions.SSLError:
			print url + ' has INVALID SSL certificate!'
			ssl_servers_file.write(url+'\n')
			url_without_https = url.replace("https://","")
			ssl._create_default_https_context = ssl._create_unverified_context() 
			cert = ssl.get_server_certificate((url_without_https, 443))
			print(cert)
			load_cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
			get_certificate_info(load_cert,newurl)
			get_curl_info(url,req.headers)

		except requests.exceptions.ConnectionError:
			print url + ' Not SSL'
			# try to send http request
			newurl = url.replace("https","http")
			try:
				req = requests.get(newurl,timeout = 0.1)
				get_curl_info(url,req.headers)
			except requests.exceptions.ConnectionError:
				print("Not a Web Server")
			except requests.exceptions.ReadTimeout:
				print ("timeout No web server at all")
		except requests.exceptions.ReadTimeout:
			print 'timeout'

def get_curl_info(url,curl_data):
	data = {}
	data['url'] = url
	print()
	data['Content-Length'] = curl_data['Content-Length']
	data['Content-Encoding'] = curl_data['Content-Encoding']
	data['Vary'] = curl_data['Vary']
	data['Keep-Alive'] = curl_data['Keep-Alive']
	data['Server'] = curl_data['Server']
	data['Connection'] = curl_data['Connection']
	data['Date'] = curl_data['Date']
	data['Content-Type'] = curl_data['Content-Type']
	json_data = json.dumps(data)
	print(json_data)

def get_certificate_info(cert,url):
	data = {}
	data['url'] = url
	data['extension'] = cert.get_extension()
	data['issuer'] = cert.getissuer()
	data['not_after'] = cert.get_notAfter()
	data['not_before'] = cert.get_notBefore()
	data['public_key'] = cert.get_pubkey()
	data['serial_number'] = cert.get_serial_number()
	data['sig_alg'] = cert.get_signature_algorithm()
	data['subject'] = cert.get_subject()
	data['version'] = cert.get_version()
	data['has_expired'] = cert.has_expired()
	json_data = json.dumps(data)
	print(json_data)


subnet_to_check = sys.argv[1]
ssl_servers_file = open(subnet_to_check.replace("/","")+"_ssl_servers.txt", "w")
counter = 10000
for ip in IPNetwork(subnet_to_check):
	if(counter == 0):
		break
	else:
		counter -= 1

	print '%s' % ip
	check_ssl('https://'+str(ip),ssl_servers_file)
ssl_servers_file.close()