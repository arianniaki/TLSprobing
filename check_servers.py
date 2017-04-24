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
import socket

def check_without_verify(url,file,subnet):
			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			try:
				req = requests.get(url, verify=False,timeout=0.2)
				print url + ' SSL certificate!'
				url_without_https = url.replace("https://","")
				try:
					cert = ssl.get_server_certificate((url_without_https, 443))
					load_cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
					subject = load_cert.get_subject()
					issued_to = str(subject.CN)
					servers_file.write(url+','+issued_to+','+subnet+'\n')
				except ssl.SSLError:
					print("SSL ERROR")
					servers_file.write(url+','+subnet+', SSL Error'+'\n')
				except requests.exceptions.SSLError:
					print("Bad SSL Handshake Error")
					servers_file.write(url+','+url+','+subnet+', SSL Handshake Error'+'\n')

				except requests.exceptions.ConnectionError:
					print("connection Error")
					# servers_file.write(url+','+url+','+subnet+', Connection Error'+'\n')

			except requests.exceptions.SSLError:
				print("Bad SSL Handshake Error")
				servers_file.write(url+','+url+','+subnet+', SSL Handshake Error'+'\n')
			except ssl.SSLError:
				servers_file.write(url+','+url+','+subnet+', SSL Error'+'\n')
				print("SSL ERROR")
			except OpenSSL.SSL.SysCallError:
				servers_file.write(url+','+url+','+subnet+', SSL SyscallError'+'\n')
				print("OpenSSL syscall error" )
			except socket.error:
				servers_file.write(url+','+url+','+subnet+', SSL Socket error'+'\n')
				print("socket error" )

			except requests.exceptions.TooManyRedirects:
				print("too many redirects")

			except requests.exceptions.ConnectionError:
				# try to send http request
				newurl = url.replace("https","http")
				try:
					req = requests.get(newurl,timeout = 0.2)
					# get_curl_info(newurl,req.headers)
					servers_file.write(newurl+','+','+subnet+'\n')
				except requests.exceptions.ConnectionError:
					# servers_file.write(newurl+','+','+subnet+','+'connection error'+'\n')
					pass
					# print("NOT SSL AND Not a Web Server")
				except requests.exceptions.ReadTimeout:
					# servers_file.write(newurl+','+','+subnet+','+'connection timeout'+'\n')
					pass
					# print ("NOT SSL timeout No web server at all")
				except requests.packages.urllib3.exceptions.InvalidHeader:
					servers_file.write(newurl+','+','+subnet+',invalid header'+'\n')
					pass
					# print("invalid header")
			except requests.exceptions.ReadTimeout:
				servers_file.write(url+','+url+','+subnet+', Timeout'+'\n')
				print 'timeout: '+url


subnet_file_name = sys.argv[1]
servers_file = open(subnet_file_name+"_servers.txt", "w")

F = open(subnet_file_name+'.txt',"r")
list_of_subnets = F.readlines()
print(list_of_subnets)
for subnet in list_of_subnets:
	for ip in IPNetwork(subnet.replace('\n','')):
		# print '%s' % ip
		check_without_verify('https://'+str(ip),servers_file,subnet)

servers_file.close()
