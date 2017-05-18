# TLSprobing
This is the course project of CSE 534
Our website can be found at:
http://arianniaki.github.io/TLSprobing/

**Goal of the Project**
Goal of the project:
The main goal of this project is to measure several factors about HTTPS servers, including supported TLS version/Ciphersuites, OS version, supported Protocols (HTTP version), and certificates advertise. We measure which versions of SSL/TLS are supported by web servers. This is important because some versions of SSL like SSL3.0 are insecure and should not be supported by servers. However, there still exist servers on the Internet which support SSL 3.0 which makes them vulnerable. Furthermore, we obtain which ciphersuites these HTTPS servers support. Ciphersuites are a combination of authentication, encryption, message authentication code and, key exchange algorithms used in the TLS protocol. Some of the algorithms used in ciphersuites also have known weaknesses. A recent related news is about the collision of SHA1 algorithm which is used in some ciphersuites. It is interesting that our measurement shows many servers still continue the usage of these insecure algorithms. In order to classify these servers, we studied what OS versions they have and we also check the adoption of HTTP/2.0 among these servers. We compare the HTTPS servers, their support of TLS, ciphersuites and certificates between several universities around the United States. We also inspect the certificates presented by these servers. Each certificate has a validation duration, issuer and support of OCSP (Online Certificate Status Protocol).

**Scope of the project**
For our study cases, we selected 18 different universities scattered around the United States and did our measurements on their web servers. Figure 3 shows their logo/name and location on the map. (Our TLS study is done for 11 universities, we will complete our study for the 18 universities as soon as possible)


**AS numbers to IP addresses conversion**
The first step to start the project was getting servers’ IP addresses. Using a CSV file of AS numbers we obtained the AS numbers of our desired universities and then gathered their ip range. Further, we used a Python script HTTPS and HTTP requests to all the ip addresses in the ip subnet ranges to find out which of these ips are web servers. A total of 4,929,792 IP addresses is examined and  33,386 responded to our queries. A detailed table is presented in the table below.


**Certificates Measurements**
For gathering information about HTTPS certificates, a script is written that using Python’s requests, SSL and crypto libraries, sends GET requests to those servers and then parses the certificate. In order to check the validity of certificates, Python’s request library is used.
From this information we extract the following: 
Who is the certificate issuer.
If the certificate is valid (self signed or expired)
The validity duration of certificate in days.
Whether or not OCSP is supported in this certificate.


**TLS Measurements**
We leverage the Requests library of python to start SSL/TLS connections with the HTTPS servers in the target universities using different versions of SSL/TLS (SSL3 up to TLS1.2). In the standard TLS handshake protocol the client sends a group of supported ciphersuites, the server, on the other hand, chooses the most strong ciphersuite from client’s list and if there is any, they start a secure connection. If they do not share a common ciphersuite, the server doesn’t start the connection.
As it is obvious, based on this handshake we cannot get enough information about supported ciphersuites of a server. To overcome this issue, we formed a complete list of existing ciphersuites using the s_client application of OpenSSL 1.0.2g. Afterward, we established TLS handshakes which propose a single ciphersuite to the server. By this means, we are able to check the supported ciphersuites and extract the complete list of supported ciphersuites for each server.
