ct = '134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9'
ct = bytes.fromhex(ct)

pt = b''
pre = b'HTB{'

key = b''   
for i in range(len(pre)):
    key+=bytes([ct[i]^pre[i]])  

for i in range(len(ct)):
    pt+=bytes([ct[i]^key[i%len(key)]])

print(pt.decode())
