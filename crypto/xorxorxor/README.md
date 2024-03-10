# Encryption
xorxorxor is a crypto challenge on hack the box. First by looking at the cipher, we see that we are using the Vigenere Cipher with a random 4 bit key. 

````Python
class XOR:
    def __init__(self):
        self.key = os.urandom(4)
    def encrypt(self, data: bytes) -> bytes:
        xored = b''
        for i in range(len(data)):
            xored += bytes([data[i] ^ self.key[i % len(self.key)]])
        return xored
    def decrypt(self, data: bytes) -> bytes:
        return self.encrypt(data)
````

# The Vigenere Cipher
The Vigenere Cipher is a comprised of a series of shift ciphers where each byte of the key corresponds to a different shift cipher. The key is repeated until the entire plaintext has been encrypted.

Shift chipers in the Vigenere Cipher encrypt by taking the XOR of the plaintext byte and the corresponding key byte. They decrypt in the same way. 
```math
\text{For each byte}: M_i,K_i,M_i'\\
Plaintext: (M_0M_1M_2...M_n)\\
Key: (K_0K_1K_2...K_m)\\
Ciphertext: (M_0'M_1'M_2'...M_n')\\
```
```math
Encryption: M_i':= M_i \text{ xor } K_{i \mod m}\\
Decryption: M_i:= M_i' \text{ xor } K_{i \mod m}\\
```

# Decyrption
Since this Vigenere Cipher has a random 4 byte key and we know the flag starts with `HTB{` which is also 4 bytes, we can compute the key. We take the XOR of the first 4 bytes of the ciphertext and the plaintext `HTB{`.
```Python
key = b''   
for i in range(len(pre)):
    key+=bytes([ct[i]^pre[i]])  
```

Once we calculate the key, we just reverse the decrypt the ciphertext with this key. This is done by taking the XOR of the ciphertext with the key.
```Python
for i in range(len(ct)):
    pt+=bytes([ct[i]^key[i%len(key)]])
```

Lastly, the key is `HTB{rep34t3d_x0r_n0t_s0_s3cur3}`