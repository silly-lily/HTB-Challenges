# Encryption

BabyEncyption is a very easy crypto challenge on hack the box.
First by looking at the encryption algorthim, we see that the plaintext is sent in bytes to the encryption algorthim. Then the text is broken down byte by byte, each byte is multiplied by 123,and then 18 is added to each of these multiplied bytes (under modulo 256). This is the same as xor encryption with a key of 123 followed by a shift cipher encryption with a key of 18.

````Python
def encryption(msg):

    ct = []

    for char in msg:

        ct.append(((123*char)+18)%256)

    return bytes(ct)
````

# Decryption
To undo this encryption, first we need to undo the caesar cipher encryption then the xor encryption. First we subtract 18 to shift the bytes back. Then we find `123^-1 = 179 [mod 256]` because `123*179 = 22017 = 1 [mod 256]`.

````Python
def decryption(msg):

    pt = []

    for char in msg:

        pt.append((179*(char-18)) % 256)

    return bytes(pt)
````

# Driver Code
Lastly we need to execute this decryption algorthim on the encrypted text to get the flag. First we transform the string of hexadecimal numbers to bytes. Then we pass it to the decryption algorthim to get the flag.

````Python
MSG = '6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921'
ct = bytes.fromhex(MSG)
pt = decryption(ct)
````