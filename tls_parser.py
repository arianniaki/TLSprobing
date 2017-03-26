#https://www.sans.org/reading-room/whitepapers/authentication/ssl-tls-hood-34297
import base64
import codecs
import dpkt
import sys
class TCPFlow():
    id = ""
    def __init__(self,srcport):
        self.id = srcport
        self.tcp_packets = []

class Packet(object):
    tcp_header = ""
    ip_header = ""
    pkt_number = 0
    size = 0
    def __init__(self,tcp_header,ip_header,number,size):
        self.tcp_header = tcp_header
        self.ip_header = ip_header
        self.pkt_number = number
        self.size = size

class IP_Header:
    ip_version = 0
    ip_headerlen = 0
    ip_total_length = 0
    ip_identification = 0
    ip_flags = 0
    ip_fragment_offset = 0
    ip_ttl = 0
    ip_protocol = 0
    header_checksum = 0
    ip_src = 0
    ip_dst = 0
    def __init__(self,ip_version,ip_headerlen,ip_total_length,ip_identification,
        ip_flags,ip_fragment_offset,ip_ttl,ip_protocol,header_checksum,ip_src,
        ip_dst):
        self.ip_version = ip_version
        self.ip_headerlen = ip_headerlen
        self.ip_total_length = ip_total_length
        self.ip_identification = ip_identification
        self.ip_flags = ip_flags
        self.ip_fragment_offset = ip_fragment_offset
        self.ip_ttl = ip_ttl
        self.ip_protocol = ip_protocol
        self.header_checksum = header_checksum
        self.ip_src = ip_src
        self.ip_dst = ip_dst

class TCP_Header:
    tcp_srcport = ""
    tcp_dstport = ""
    tcp_seqnum = ""
    tcp_acknum = ""
    tcp_headerlen = ""
    tcp_flags = ""
    tcp_windowsize = ""
    tcp_checksum = ""
    tcp_urgentpointer = ""
    tcp_timestampvalue = ""
    def __init__(self,tcp_srcport,tcp_dstport,tcp_seqnum,tcp_acknum,
        tcp_headerlen,tcp_flags,tcp_windowsize,tcp_checksum,tcp_urgentpointer,tcp_timestampvalue):
        self.tcp_srcport = tcp_srcport
        self.tcp_dstport = tcp_dstport
        self.tcp_seqnum = tcp_seqnum
        self.tcp_acknum = tcp_acknum
        self.tcp_headerlen = tcp_headerlen
        self.tcp_flags = tcp_flags
        self.tcp_windowsize = tcp_windowsize
        self.tcp_checksum = tcp_checksum
        self.tcp_urgentpointer = tcp_urgentpointer
        self.tcp_timestampvalue = tcp_timestampvalue

pcap_name = sys.argv[1]
print(pcap_name)
f = open(str(pcap_name)+'.pcap')
hexlify = codecs.getencoder('hex')
pcap = dpkt.pcap.Reader(f)
hexified_bytes = []
for item in pcap:
    hexified_bytes.append(hexlify(item[1]))

def parse_ip(ip_hex):
    ip_header = IP_Header(ip_hex[0],ip_hex[1],ip_hex[3:7],ip_hex[8:12],ip_hex[12:14],
                        ip_hex[14:16],ip_hex[16:18],ip_hex[18:20],ip_hex[20:24],ip_hex[24:32],ip_hex[32:40])
    return ip_header

def parse_tcp(tcp_hex):
    # different header sizes
    if(int(tcp_hex[24:26],16) == 240):
        tcp_header = TCP_Header(int(tcp_hex[0:4],16),int(tcp_hex[4:8],16),int(tcp_hex[8:16],16),int(tcp_hex[16:24],16),
            int(tcp_hex[24:26],16),bin(int(tcp_hex[26:28], 16))[2:].zfill(8),int(tcp_hex[28:32],16),int(tcp_hex[32:36],16),int(tcp_hex[36:40],16),int(tcp_hex[48:56],16))


    if(int(tcp_hex[24:26],16) == 208):
        tcp_header = TCP_Header(int(tcp_hex[0:4],16),int(tcp_hex[4:8],16),int(tcp_hex[8:16],16),int(tcp_hex[16:24],16),
            int(tcp_hex[24:26],16),bin(int(tcp_hex[26:28], 16))[2:].zfill(8),int(tcp_hex[28:32],16),int(tcp_hex[32:36],16),int(tcp_hex[36:40],16),int(tcp_hex[48:56],16))


    if(int(tcp_hex[24:26],16) == 176):
        tcp_header = TCP_Header(int(tcp_hex[0:4],16),int(tcp_hex[4:8],16),int(tcp_hex[8:16],16),int(tcp_hex[16:24],16),
            int(tcp_hex[24:26],16),bin(int(tcp_hex[26:28], 16))[2:].zfill(8),int(tcp_hex[28:32],16),int(tcp_hex[32:36],16),int(tcp_hex[36:40],16),int(tcp_hex[64:72],16))


    if(int(tcp_hex[24:26],16) == 160):
        tcp_header = TCP_Header(int(tcp_hex[0:4],16),int(tcp_hex[4:8],16),int(tcp_hex[8:16],16),int(tcp_hex[16:24],16),
            int(tcp_hex[24:26],16),bin(int(tcp_hex[26:28], 16))[2:].zfill(8),int(tcp_hex[28:32],16),int(tcp_hex[32:36],16),int(tcp_hex[36:40],16),int(tcp_hex[56:64],16))
    if(int(tcp_hex[24:26],16) == 128):
        tcp_header = TCP_Header(int(tcp_hex[0:4],16),int(tcp_hex[4:8],16),int(tcp_hex[8:16],16),int(tcp_hex[16:24],16),
            int(tcp_hex[24:26],16),bin(int(tcp_hex[26:28], 16))[2:].zfill(8),int(tcp_hex[28:32],16),int(tcp_hex[32:36],16),int(tcp_hex[36:40],16),int(tcp_hex[48:56],16))

    if(int(tcp_hex[24:26],16) == 80):
        tcp_header = TCP_Header(int(tcp_hex[0:4],16),int(tcp_hex[4:8],16),int(tcp_hex[8:16],16),int(tcp_hex[16:24],16),
            int(tcp_hex[24:26],16),bin(int(tcp_hex[26:28], 16))[2:].zfill(8),int(tcp_hex[28:32],16),int(tcp_hex[32:36],16),int(tcp_hex[36:40],16),0)
    return tcp_header


def tcp_flag(tcp_bin):
    flags = []
    if(tcp_bin[0] == "1"):
        flags.append("CWR")
    if(tcp_bin[1] == "1"):
        flags.append("ECN-ECHO")
    if(tcp_bin[2] == "1"):
        flags.append("URGENT")
    if(tcp_bin[3] == "1"):
        flags.append("ACK")
    if(tcp_bin[4] == "1"):
        flags.append("PUSH")
    if(tcp_bin[5] == "1"):
        flags.append("RESET")
    if(tcp_bin[6] == "1"):
        flags.append("SYN")
    if(tcp_bin[7] == "1"):
        flags.append("FIN")
    return flags

def get_tcp_header_len(tcp_hex):
    return ((int(tcp_hex[24:26],16))/8)*2

def ip_extractor(ip_hex):
    ip=""
    for i in range(0,len(ip_hex),2):
        ip += str(int(ip_hex[i:i+2],16))
        ip += "."
    return ip[:-1]

def determine_protocol(tls_hex):
    protocol = tls_hex[2:6]
    print(protocol)
    if(protocol == "0300"):
        print("SSL")
    if(protocol == "0301"):
        print("TLS1.0")
    if(protocol == "0302"):
        print("TLS1.1")
    if(protocol == "0303"):
        print("TLS1.2")
    len = tls_hex[6:10]
    print(len)
    # i = int(len, 16)
    # print i


def determine_handshake_messagetype(tls_hex):
    print(tls_hex[10:12])
    handshake = tls_hex[10:12]
    if(handshake == "01"):
        print("Client Hello")
    if(handshake == "02"):
        print("Server Hello")
    if(handshake == "0b"):
        print("Certificate")
    if(handshake == "0c"):
        print("Server Key Exchange")
    if(handshake == "0c"):
        print("Server Key Exchange")
    if(handshake == "0e"):
        print("Server Hello Done")
    if(handshake == "10"):
        print("Client Key Exchange")
    if(handshake == "14"):
        print("Finished")
    len = tls_hex[12:18]
    print(len)
    


def determine_handshake(tls_hex):
    if(tls_hex[10:12] == "02"):
        return 1

def determine_ciphersuites(tls_hex):
    print("begin ciphersuites list")
    ciphersuite_len = (tls_hex[152:156])
    i = int(ciphersuite_len, 16)
    print ciphersuite_len,i
    print(tls_hex[156:156+i*2])

        
print ('------------------')
i = 0
tcp_headers = []
ip_headers = []
packets = []
for a in hexified_bytes:
    ip_header = parse_ip(a[0][28:])
    tcp_header_len = get_tcp_header_len(a[0][68:132])
    tcp_header = parse_tcp(a[0][68:68+tcp_header_len*2])

    i += 1
    packet = Packet(tcp_header,ip_header,i,a[1])
    packets.append(packet)

    print("-------", i)
    tls_header = a[0][68+tcp_header_len*2:]
    # This is a Handshake record
    if(tls_header[:2] == '16'):
        protocol_version = determine_protocol(a[0][68+tcp_header_len*2:])
        handshake_type = determine_handshake_messagetype(a[0][68+tcp_header_len*2:])
        ciphersuites = determine_ciphersuites(a[0][68+tcp_header_len*2:])