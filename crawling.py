from bs4 import *
import requests as rq
import os

r1 = rq.get("https://www.zedge.net/wallpapers")
soup = BeautifulSoup(r1.text, "html.parser")

links = []

x = soup.select('img[src^="https://fsa.zobj.net/crop.php?"]')

for img in x:
    links.append(img['src'])

if os.path.isdir('E:\Projects and Other\Image crawler Python\zedge_wallpaper'):
    print("Directory Exists")
else:
    os.mkdir('zedge_wallpaper')

i = 1

for index, img_link in enumerate(links):
    if i <= 10:
        img_data = rq.get(img_link).content
        with open("zedge_wallpaper/"+str(index+1)+'.jpg','wb+') as f:
            f.write(img_data)
        i += 1
    else:
        f.close
        break
