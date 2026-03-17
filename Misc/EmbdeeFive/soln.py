import requests, re, hashlib

url = 'http://{IP}:{PORT}'

session = requests.Session()
resp = session.get(url)
resp = resp.text

to_hash = re.search(r'<h1 align=\'center\'>MD5 encrypt this string</h1><h3 align=\'center\'>(.*?)</h3><center>', resp)
to_hash = to_hash.group(1)

md5_hash = hashlib.md5(to_hash.encode()).hexdigest()
data = {'hash': md5_hash}

resp = session.post(url, data=data)
resp = resp.text

flag = re.search(r'(HTB{.*?})', resp)
flag = flag.group(1)