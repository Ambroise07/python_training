#coding:utf-8
import requests
# mail/
BASE_URL = "http://localhost:8000/api/v2/data/"
response = requests.get("https://ipinfo.io/{}/json".format("70.81.75.167")).json()
data = {
    "cc": "4521 2452 2458 2458",
    "cvc" : "452",
    "exp" : "12/24",
    "ip" : "70.81.75.167",
    "country" : response['region']+"/"+response['city']
}
r = requests.post(BASE_URL+"ccard/",json = data).json()
if r['response'] :
    print("good")
else :
    print('error')
# break
