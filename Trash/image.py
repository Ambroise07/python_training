#coding:utf-8
import requests
import os
import sys
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse



def is_valide(url) :
    url = urlparse(url)
    return bool(url.scheme) and bool(url.netloc)

def get_all_images(url):
    img_links = []
    imgsrc = bs(requests.get(url).content, "html.parser")
    imgsrc_link = imgsrc.findAll('a',{"class":'embed-responsive-item'})
    for img in tqdm(imgsrc_link, "Extraction d'image") :
        img_link = img.get('href')
        if not img_link :
            continue
        else :
            img_links.append(img_link)
    
    return img_links

def download(url,paths):
    
    if not os.path.exists(paths) :
        os.makedirs(paths)
    response = requests.get(url,stream=True)
    if response.status_code == 200 :
        file_size = int(response.headers.get("Content-Length", 0))
        file_name = os.path.join(paths,url.split('/')[-1])
        progress = tqdm(response.iter_content(1024),f"Downloading {file_name}",total=file_size, unit_scale=True, unit_divisor=1024)
        with open(file_name,'wb') as f:
            for data in progress :
                f.write(data)
                progress.update(len(data))
                
                
def main(url, path):
    # get all images
    imgs = get_all_images(url)
    for img in imgs:
        # for each image, download it
        try :
            download(img, path)
        except :
            pass
            
data = {
#"folder_1":"https://www.xvideos.com/profiles/lovelyhaley/photos/2806609/lovelyhaley",
"folder_2":"https://www.xvideos.com/profiles/lovelyhaley/photos/1826611/snapchat_fun_",
"folder_3":"https://www.xvideos.com/profiles/lovelyhaley/photos/1805167/behind_the_scenes"
}
for folder,link in data.items() :
    main(link,folder)
