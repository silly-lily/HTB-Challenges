### xorxorxor

Who needs AES when you have XOR?

Challenge Files: [challenge.py](challenge.py), [output.txt](output.txt)<br><br>

Category: Crypto<br>
Difficulty: Easy

---

#### Encryption

First by looking at the `challenge.py` file, we see that we are using the Vigenère Cipher with a random 4 bit key.

````Python
# challenge.py
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

The Vigenère Cipher encrypts by shifting each letter of the plaintext based on a repeating key of a fixed length. Each letter in the plaintext is shifted forward according to the corresponding letter in the key, and when the last letter of the key is reached, the encryption restarts from the beginning of the key. For example, encrypting the word "STRAWBERRY" using a Vigenère Cipher with a key length of three, we have:

| Plaintext  | S  | T  | R  | A  | W  | B  | E  | R  | R  | Y  |
|------------|----|----|----|----|----|----|----|----|----|----|
| Key        | B  | A  | X  | B  | A  | X  | B  | A  | X  | B  |
| Ciphertext | T  | T  | O  | B  | W  | Y  | F  | R  | O  | Z  |



---

#### Decryption

Since this the flag was encrypted with a 4 byte key and the plaintext flag starts with `HTB{` (which is also 4 bytes), we can compute the key and then decrypt. To compute the key we xor the first four bytes of the ciphertext with `HTB{`:


```Python
pre = b'HTB{'

key = b''   
for i in range(len(pre)):
    key+=bytes([ct[i]^pre[i]])  
```

Once we calculate the key, we use it to decrypt the flag:

```Python
for i in range(len(ct)):
    pt+=bytes([ct[i]^key[i%len(key)]])
```

---

#### Flag
> HTB{rep34t3d_x0r_n0t_s0_s3cur3}

---
