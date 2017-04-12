# TLSprobing
This is the course project of CSE 534

***Project Progress

  1- Finding universities' IPs
  
      using the ASnumber of universities, we found their ip ranges
      
  2- Checking supported TLS protocols, Ciphersuits by webservers
  
      using a set of scripts we sent hello client (the first message of a tls connection) to these ip addresses using 4 tls         protocol versions and 100 different cipher suites, In order to check the support of the tls protocol and ciphersuite by       the web servers
      
  3- Certificates' Study
  
      using a set of scripts we fetched the certificate of the https web servers and checked their validity and other               certificate features such as the period of validity, their issuer, and etc.
      
  4- Web Servers' Study
  
      to gather more data about the web servers we also found out which OS the server is running and we plan to determine the       set of http protocol versions they support
