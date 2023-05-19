from Crypto.Cipher import AES
with open("/mnt/c/Users/barsh/Downloads/Bi0s/flag.bin",'rb') as file:
    data = file.read()
key = b'BatmanKn1ghtfall'
iv = b'fl4g{n0t_4_fl4g}' 

def decrypt(data,key,iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(data)
    return decrypted

print(decrypt(data, key, iv))
open("/mnt/c/Users/barsh/Downloads/Bi0s/updatedchall/flag.png","wb").write(decrypt(data,key,iv))