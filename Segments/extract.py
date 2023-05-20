from scapy.all import *
f = rdpcap("/mnt/c/Users/barsh/Downloads/Bi0s/chall/chall/Segments/challenge.pcapng")
b= bytes()
for i in f:
    if TCP in i and IP in i :
        if i[IP].dst == "172.18.48.1":
                try:
                    b+=bytes(i[IP].load)
                except:
                    continue

print(b)
open("/mnt/c/Users/barsh/Downloads/Bi0s/chall/chall/Segments/flag.png","wb").write(b)