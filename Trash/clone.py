#coding:utf-8
from os import system

url_list = {
    #"escorte" : "https://www.escorte.com/auth/login/",
    "shop":"https://indilademo.netlify.app/indila/index-5#"


}
#https://indilademo.netlify.app/indila/index-5#
for key ,value in url_list.items() :
    cmd = "curl '{0}' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' > {1}.html".format(value,key)
    #cmd = "curl '{0}' -H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/83.0.4103.116 Mobile/15E148 Safari/604.1' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' > {1}.html".format(value,key)
    system(cmd)