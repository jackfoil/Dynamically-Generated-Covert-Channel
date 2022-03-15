from scapy.all import *

##a=scapy.IP("142.251.46.142")
##print(a)
##send(IP(src="10.0.99.100",dst="10.1.99.100")/ICMP()/"Hello World")
##send(IP(dst='8.8.8.8')/TCP(dport=53, flags='S'))
#for i in range(50):
    #sr1(IP(dst="142.251.46.142")/TCP(sport=RandShort(),dport=55,flags="S"),verbose=1, timeout=3)
    #sr1(IP(dst="142.251.46.142")/ICMP())
    #sr(IP(dst="142.251.46.142")/ICMP(), retry=0, timeout=1)



t=AsyncSniffer(store=True)
t.start()

L= sr1(IP(dst="google.com")/ICMP(), retry=0, timeout=1)
print(L)
print()
t.stop()
print(ls(L))
print()
print(L.show())
