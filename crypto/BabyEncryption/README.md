### Baby Encryption

You are after an organised crime group which is responsible for the illegal weapon market in your country. As a secret agent, you have infiltrated the group enough to be included in meetings with clients. During the last negotiation, you found one of the confidential messages for the customer. It contains crucial information about the delivery. Do you think you can decrypt it?

Challenge Files: [chall.py](chall.py), [msg.enc](msg.enc)<br><br>

Category: Crypto<br>
Difficulty: Very Easy

---

#### Encryption
We look at the encryption algorithm in the `chall.py` file. We see that the plaintext is broken down byte by byte, each byte is multiplied by $123$, and then $18$ is added to each of these multiplied bytes (under modulo $256$). This is the same as xor encryption with a key of $123$ followed by a shift cipher encryption with a key of $18$.

```Python
# chall.py
def encryption(msg):

    ct = []

    for char in msg:

        ct.append(((123*char)+18)%256)

    return bytes(ct)
```

---

#### Decryption
To decrypt, first we need to undo the caesar cipher encryption then undo the xor encryption. First we subtract $18$ and then multiply by the inverse of $123$  (under modulo $256$):



```math
\begin{alignedat}{2}
& ct \equiv (msg*123)+18 & \pmod{256}\\
& ct-18 \equiv msg*123 & \pmod{256}\\
& msg \equiv (ct-18)*123^{-1} &\pmod{256}\\
& msg \equiv (ct-18)*179 & \pmod{256}\\
\end{alignedat}
```

</div>

---

## Flag
> HTB{l00k_47_y0u_r3v3rs1ng_3qu4710n5_c0ngr475}


```Python
# soln.py
def decryption(msg):

    pt = []

    for char in msg:

        pt.append((179*(char-18)) % 256)

    return bytes(pt)
```

---