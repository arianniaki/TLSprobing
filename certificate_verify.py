import requests
from netaddr import IPNetwork
import json
import sys
from OpenSSL import crypto
import ssl
import json
import subprocess
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import OpenSSL

def check_ssl(ip,url,subnet ):
			if(url != ''):
				print(url)
			else:
				print(url + ' it is empty')
			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			try:
				req = requests.get(url, verify=True,timeout=0.5)

				print url + ' has a valid SSL certificate!'
				# servers_file.write(url+'\n')
				url_without_https = url.replace("https://","")
				try:
					cert = ssl.get_server_certificate((url_without_https, 443))
					load_cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
					get_certificate_info(load_cert,url)
					get_curl_info(url,req.headers)
				except ssl.SSLError:
					print("SSL ERROR ______ __ _ _ ")
				except requests.exceptions.SSLError:
					print("sni ERROR")
			except requests.exceptions.TooManyRedirects:
				print("too many redirect")

			except requests.exceptions.SSLError:
				print url + ' has INVALID SSL certificate!'
				# servers_file.write(url+'\n')
				url_without_https = url.replace("https://","")

				p = subprocess.Popen(["timeout","30","openssl", "s_client",'-connect',url_without_https+":443"], stdout=subprocess.PIPE)
				out, err = p.communicate()
				out_without_n = out.replace('\n','!@#$&*()')
				cert = re.findall(r'-----BEGIN.*END.CERTIFICATE-----',out_without_n)
				if(len(cert)>0):
					print('============')
					print(cert)
					print('============')
					cert = cert[0].replace('!@#$&*()','\n')
					load_cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
					get_certificate_info(load_cert,url)
					# print(cert)
				p = subprocess.Popen(["curl", "-k" ,url, "--head","-m","30"],stdout=subprocess.PIPE)
				out, err = p.communicate()
				print(out)


				# ssl._create_default_https_context = ssl._create_unverified_context() 
				# cert = ssl.get_server_certificate((url_without_https, 443))
				# print(cert)
				
				# get_curl_info(url,req.headers)

			except requests.exceptions.ConnectionError:
				# try to send http request
				newurl = url.replace("https","http")
				try:
					req = requests.get(newurl,timeout = 0.1)
					get_curl_info(url,req.headers)
				except requests.exceptions.ConnectionError:
					pass
					# print("NOT SSL AND Not a Web Server")
				except requests.exceptions.ReadTimeout:
					pass
					# print ("NOT SSL timeout No web server at all")
			except requests.exceptions.ReadTimeout:
				print 'timeout'

def get_curl_info_invalidcert(url,curl_date):
	data = {}
	data['url'] = url
	
def get_curl_info(url,curl_data):
	data = {}
	data['url'] = url
	print('HTTP')
	try:
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
	except KeyError:
		print(url+'   key error given')

def get_certificate_info(cert,url):
	print(cert)
	data = {}
	data['url'] = url
	# data['extension'] = cert.get_extension()
	subject = cert.get_subject()
	data['issued_to'] = str(subject.CN)
	issuer = cert.get_issuer()
	issued_by = issuer.CN
	print(issued_by)
	data['issuer'] = str(cert.get_issuer())
	data['not_after'] = cert.get_notAfter()
	data['not_before'] = cert.get_notBefore()
	# data['public_key'] = cert.get_pubkey()
	data['serial_number'] = cert.get_serial_number()
	data['sig_alg'] = cert.get_signature_algorithm()
	data['subject'] = str(cert.get_subject())
	data['version'] = cert.get_version()
	data['has_expired'] = cert.has_expired()
	# print(data)
	json_data = json.dumps(data)
	print(json_data)


# req = requests.get('https://31.13.71.36', verify=True,timeout=0.1)
# subnet_to_check = sys.argv[1]

subnet_file_name = sys.argv[1]
# servers_file = open(subnet_file_name+"_servers.txt", "w")

F = open(subnet_file_name,"r") 
list_of_servers = F.readlines()
# print(list_of_servers)
for server in list_of_servers:
	ip,url,subnet = server.split(',')
	print(ip+'  '+url+' '+subnet)
	check_ssl(ip,url,subnet)

# servers_file.close()