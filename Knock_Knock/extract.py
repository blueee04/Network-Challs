from scapy.all import *
f = rdpcap("/mnt/c/Users/barsh/Downloads/Bi0s/chall/chall/Knock_Knock/chall.pcap")
b= bytes()
s = ""
for i in f:
    if ICMP in i and IP in i :
        if i[IP].dst == "172.16.100.101":
                b+=bytes(i[IP].load)
                s = s + chr(len(i[IP].load))
print(b)
print(s)
open("flag.bin","wb").write(b)