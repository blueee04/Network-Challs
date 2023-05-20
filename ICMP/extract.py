from scapy.all import *
f = rdpcap("/mnt/c/Users/barsh/Downloads/Bi0s/chall/chall/ICMP/chall.pcapng")
b= bytes()
for i in f:
    if ICMP in i and IP in i :
        if i[IP].dst == "192.168.121.1":
            if(len(i[IP].load)==64):
                 b+=bytes(i[IP].load)

print(b)
open("/mnt/c/Users/barsh/Downloads/Bi0s/chall/chall/ICMP/flag.gif","wb").write(b)