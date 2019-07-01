![GitHub stars](https://img.shields.io/github/stars/veerendra2/dictionaries.svg?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/veerendra2/dictionaries.svg?style=for-the-badge)
# Python Dictionaries
Simple python dictionaries for HTTP, FTP return codes and TCP ports, etc. Usefull when code throws number(HTTP return code), instead of diplaying return code number like `404`, show message what it means. 

In same way, when we are doing some networking stuff in python like collecting network connections, with help of `TCPPorts.py` we can identify destination service in it. For example, we have collected network connections(with tools like `conntrack`),the current machine made connection to another machine with destination port `80` which means a web server. Some we can guess like `80`,`8080` and some we dont know, with `TCPPorts.py` we can display the service name instead of port number.

#### Example code snippet
```
import requests
#Local Imports
import HTTPStatusCodes

headers = {'content-type': 'application/json'}
url="http://www.google.com" #Example URL
data={"data":"Your Data"}
response = requests.post(url, data=data,headers=headers)
print response
if response.status_code in HTTPStatusCodes.codes:
   print HTTPStatusCodes.codes[response.status_code][0]
   print "Description",HTTPStatusCodes.codes[response.status_code][1]
```

* Collected TCP port from [http://www.iana.org](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)
* Collected HTTP status codes from [wikipedia](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
* Collected FTP returned codes from [wikipedia](https://en.wikipedia.org/wiki/List_of_FTP_server_return_codes)
* Collected TCP connections states from [kernel.org](http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/tree/include/net/tcp_states.h?id=HEAD)
