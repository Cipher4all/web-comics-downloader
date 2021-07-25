from bs4 import BeautifulSoup
import os
import requests
import shutil

print('Put the web comic you want to download:')
url = input('>')
print(f'Printing the web comic:{url}')
pathname = input('Enter the filepath:')
os.makedirs(pathname)

while not url.endswith('#'):    
    print('Downloading page %s...'%url)
    web_comics = requests.get(url)
    soup = BeautifulSoup(web_comics.text, 'lxml')
    images = soup.find('img', class_ = 'comicimage')
    original = images.attrs['src']
    print('Downloading image %s..'%(original))
    res = requests.get(original, stream = True)
    imgfile = os.path.join(pathname, os.path.basename(original))
    if res.status_code == 200:
        with open(imgfile, 'wb') as f:
            res.raw.decode_content = True
            shutil.copyfileobj(res.raw, f)
            
    link = soup.find('li', class_ = 'prev')
    url = "http://www.lefthandedtoons.com/" + link.find('a').get('href')

print('Done')
            