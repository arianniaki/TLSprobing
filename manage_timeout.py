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
				req = requests.get(url, verify=False,timeout=5)
				print url + ' SSL certificate!'
				url_without_https = url.replace("https://","")
				try:
					cert = ssl.get_server_certificate((url_without_https, 443))
					load_cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
					subject = load_cert.get_subject()
					issued_to = str(subject.CN)
					file.write(url+','+issued_to+','+subnet+'\n')
				except ssl.SSLError:
					print("SSL ERROR",url)
					file.write(url+',OPENSSL,'+subnet+'\n')
				except requests.exceptions.SSLError:
					print("Bad SSL Handshake Error",url)
					file.write(url+',OPENSSL,'+subnet+'\n')
				except requests.exceptions.ConnectionError:
					print("connection Error",url)
					file.write(url+',OPENSSL,'+subnet+'\n')

			except requests.exceptions.SSLError:
				print("Bad SSL Handshake Error",url)
				file.write(url+',OPENSSL,'+subnet+'\n')
				
			except ssl.SSLError:
				print("SSL ERROR", url)
				file.write(url+',OPENSSL,'+subnet+'\n')
			except OpenSSL.SSL.SysCallError:
				print("OpenSSL syscall error",url)
				file.write(url+',OPENSSL,'+subnet+'\n')
			except socket.error:
				print("socket error",url)
				file.write(url+',OPENSSL,'+subnet+'\n')

			except requests.exceptions.TooManyRedirects:
				print("too many redirects",url)
				file.write(url+',OPENSSL,'+subnet+'\n')
			except requests.exceptions.ConnectTimeout:
				print("connect timeout")
				file.write(url+',OPENSSL,'+subnet+'\n')

			except requests.exceptions.ConnectionError:
				# try to send http request
				newurl = url.replace("https","http")
				try:
					req = requests.get(newurl,timeout = 5)
					# get_curl_info(newurl,req.headers)
					W.write(newurl+','+','+subnet+'\n')
				except requests.exceptions.TooManyRedirects:
					print("too many redirects")
				except requests.exceptions.ConnectionError:
					# servers_file.write(newurl+','+','+subnet+','+'connection error'+'\n')
					print("connection error",url)
					pass
					# print("NOT SSL AND Not a Web Server")
				except requests.exceptions.ReadTimeout:
					print("read timeout",url)
					# servers_file.write(newurl+','+','+subnet+','+'connection timeout'+'\n')
					pass
					# print ("NOT SSL timeout No web server at all")
				except requests.packages.urllib3.exceptions.InvalidHeader:
					print("invalid header",url)
					pass
					# print("invalid header")
			except requests.exceptions.ReadTimeout:
				print 'timeout: '+url
				file.write(url+',OPENSSL,'+subnet+'\n')


subnet_file_name = sys.argv[1]


F = open(subnet_file_name,"r") 
list_of_servers = F.readlines()
W = open("final_"+subnet_file_name,"a") 
servers =[]
for line in list_of_servers:
		if("Timeout" in line):
			# print("go check timeout again")
			url,garbage,subnet,error = line.split(',')
			a = check_without_verify(url,W,subnet)
			continue
		if("SSL Handshake Error" in line):
			ssl_version=ssl.PROTOCOL_SSLv3
			# print("go check ssl handshake again")
			url,garbage,subnet,error = line.split(',')
			a = check_without_verify(url,W,subnet)
			continue
		else:
			W.write(line)
			# servers.append(line)

for a in servers:
	print(a)

W.close()

