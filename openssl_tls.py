# https://www.feistyduck.com/library/openssl-cookbook/online/ch-testing-with-openssl.html
import subprocess
import json
import sys
import time
import re


import subprocess
ciphers = ['ECDHE-RSA-AES256-GCM-SHA384','ECDHE-ECDSA-AES256-GCM-SHA384','ECDHE-RSA-AES256-SHA384','ECDHE-ECDSA-AES256-SHA384','ECDHE-RSA-AES256-SHA','ECDHE-ECDSA-AES256-SHA','SRP-DSS-AES-256-CBC-SHA','SRP-RSA-AES-256-CBC-SHA','SRP-AES-256-CBC-SHA','DH-DSS-AES256-GCM-SHA384','DHE-DSS-AES256-GCM-SHA384','DH-RSA-AES256-GCM-SHA384','DHE-RSA-AES256-GCM-SHA384','DHE-RSA-AES256-SHA256','DHE-DSS-AES256-SHA256','DH-RSA-AES256-SHA256','DH-DSS-AES256-SHA256','DHE-RSA-AES256-SHA','DHE-DSS-AES256-SHA','DH-RSA-AES256-SHA','DH-DSS-AES256-SHA','DHE-RSA-CAMELLIA256-SHA','DHE-DSS-CAMELLIA256-SHA','DH-RSA-CAMELLIA256-SHA','DH-DSS-CAMELLIA256-SHA','ECDH-RSA-AES256-GCM-SHA384','ECDH-ECDSA-AES256-GCM-SHA384','ECDH-RSA-AES256-SHA384','ECDH-ECDSA-AES256-SHA384','ECDH-RSA-AES256-SHA','ECDH-ECDSA-AES256-SHA','AES256-GCM-SHA384','AES256-SHA256','AES256-SHA','CAMELLIA256-SHA','PSK-AES256-CBC-SHA','ECDHE-RSA-AES128-GCM-SHA256','ECDHE-ECDSA-AES128-GCM-SHA256','ECDHE-RSA-AES128-SHA256','ECDHE-ECDSA-AES128-SHA256','ECDHE-RSA-AES128-SHA','ECDHE-ECDSA-AES128-SHA','SRP-DSS-AES-128-CBC-SHA','SRP-RSA-AES-128-CBC-SHA','SRP-AES-128-CBC-SHA','DH-DSS-AES128-GCM-SHA256','DHE-DSS-AES128-GCM-SHA256','DH-RSA-AES128-GCM-SHA256','DHE-RSA-AES128-GCM-SHA256','DHE-RSA-AES128-SHA256','DHE-DSS-AES128-SHA256','DH-RSA-AES128-SHA256','DH-DSS-AES128-SHA256','DHE-RSA-AES128-SHA','DHE-DSS-AES128-SHA','DH-RSA-AES128-SHA','DH-DSS-AES128-SHA','DHE-RSA-SEED-SHA','DHE-DSS-SEED-SHA','DH-RSA-SEED-SHA','DH-DSS-SEED-SHA','DHE-RSA-CAMELLIA128-SHA','DHE-DSS-CAMELLIA128-SHA','DH-RSA-CAMELLIA128-SHA','DH-DSS-CAMELLIA128-SHA','ECDH-RSA-AES128-GCM-SHA256','ECDH-ECDSA-AES128-GCM-SHA256','ECDH-RSA-AES128-SHA256','ECDH-ECDSA-AES128-SHA256','ECDH-RSA-AES128-SHA','ECDH-ECDSA-AES128-SHA','AES128-GCM-SHA256','AES128-SHA256','AES128-SHA','SEED-SHA','CAMELLIA128-SHA','IDEA-CBC-SHA','PSK-AES128-CBC-SHA','ECDHE-RSA-RC4-SHA','ECDHE-ECDSA-RC4-SHA','ECDH-RSA-RC4-SHA','ECDH-ECDSA-RC4-SHA','RC4-SHA','RC4-MD5','PSK-RC4-SHA','ECDHE-RSA-DES-CBC3-SHA','ECDHE-ECDSA-DES-CBC3-SHA','SRP-DSS-3DES-EDE-CBC-SHA','SRP-RSA-3DES-EDE-CBC-SHA','SRP-3DES-EDE-CBC-SHA','EDH-RSA-DES-CBC3-SHA','EDH-DSS-DES-CBC3-SHA','DH-RSA-DES-CBC3-SHA','DH-DSS-DES-CBC3-SHA','ECDH-RSA-DES-CBC3-SHA','ECDH-ECDSA-DES-CBC3-SHA','DES-CBC3-SHA','PSK-3DES-EDE-CBC-SHA']
# tls_version = sys.argv[2]
tls_versions = ['-ssl3','-tls1','-tls1_1','-tls1_2']

def get_client_hello_info(s_client_out,url):
	out_without_n = s_client_out.replace('\n','!@#$&*()')
	info = re.findall(r'Protocol.*Session-ID:',out_without_n)
	info = info[0].replace('Session-ID:','')
	print(info)
	protocols = re.findall(r'Protocol.*Cipher',info)
	protocol = protocols[0].replace('Cipher','')
	protocol = protocol.replace('!@#$&*()','')
	protocol = protocol.replace('Protocol  : ','')
	ciphers = re.findall(r'Cipher.*',info)
	cipher = ciphers[0].replace('Cipher    : ','')
	cipher = cipher.replace('!@#$&*()','')

	data = {}
	data['url'] = url
	print()
	data['Protocol'] = protocol.strip()
	data['Cipher'] = cipher.strip()
	json_data = json.dumps(data)
	print(json_data)





# print(ciphers)
# print(tls_version)
for ver in tls_versions:
	for cipher in ciphers:
		print('...............................')
		print(ver+'___: '+cipher)
		p = subprocess.Popen(["timeout","30","openssl", "s_client",'-cipher',cipher ,ver,'-connect','130.245.27.37:443','-status'], stdout=subprocess.PIPE)
		out, err = p.communicate()
		print('=======')
		print(out)
		print('::::end:::')
		get_client_hello_info(out,'130.245.27.37')
		print(">>>>>>>>>>>>>>>>\n")
		time.sleep(1)

#print out
# print(out)
