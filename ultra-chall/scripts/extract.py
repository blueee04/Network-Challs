from scapy.all import *
f = rdpcap("/mnt/c/Users/barsh/Downloads/Bi0s/updatedchall/ICMP.pcapng")
b= bytes()
for i in f:
    if ICMP in i and IP in i :
        if i[IP].dst == "10.0.0.2":
                b+=bytes(i[IP].load)
print(b)
open("flag.bin","wb").write(b)