#coding:utf-8
import requests
	
import requests

url = "http://httpbin.org/ip"
proxy_host = "proxy.crawlera.com"
proxy_port = "8010"
proxy_auth = ":"
proxies = {
       "https": "https://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
       "http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)
}

r = requests.get(url, proxies=proxies, verify=False)
"""proxies = {
 "http": "94.23.196.68:3128",
 "https":"94.23.196.68:3128",
}
res = requests.get("http://toscrape.com", proxies=proxies)"""
print(r)
#133c9UQbHtfrJN8uKyNzzEeQegrE3AkCMs
/home/ambroise/.config/google-chrome/Default

#683D58886647C90CA9AC1B8A42A6638570D45B6A812D8CF4B5699D32F1657632CBC289C767BD99A09F16BA54C4