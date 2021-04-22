#coding:utf-8
import requests
# mail/
BASE_URL = "http://localhost:8000/api/v2/data/"


clean_data = []    
clean_mail = []    
with open("f_data_","r") as datas:
    for i in datas.readlines() :
        line = i.split("->")
        email,ip = line
        response = requests.get("https://ipinfo.io/{}/json".format(ip.strip())).json()
        if response['country'] != "BJ" :
            print(response['country'])
            data = {
                "email" : email.strip(),
                "ip" : ip.strip(),
                "country" : response['region']+"/"+response['city']
            }
            r = requests.post(BASE_URL+"mail/",json = data).json()
            if r['response'] :
                print("good")
            else :
                print('error')
            # break
