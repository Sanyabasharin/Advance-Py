import requests
#import time
from bs4 import BeautifulSoup
headers = {"User-Agent": "ittensive-python-couses/1.0 (+https://www.ittenasive.com)"}
r = requests.get("https://video.ittensive.com/data/018-python-advanced/beru.ru/", headers=headers)

html = BeautifulSoup(r.content)
print (html)
links = html.find_all("a", {"class": "grid-snippet__react-link"})
print('links', links)

link_263 = ''
link_452 = ''
for link in links:
    if str(link).find("Саратов 263") > -1:
        link_263 = link["href"]
    if str(link).find("Саратов 452") > -1:
        link_452 = link["href"]


print('link_263 =', link_263)
print('link_452 =', link_452)

def find_volume (link):
    r = requests.get("https://video.ittensive.com/data/018-python-advanced/beru.ru/" + link)
    html = BeautifulSoup(r.content)
    volume = html.find_all("span", {"class": "_112Tad-7AP"})
    return int(''.join(i for i in volume[2].get_text() if i.isdigit()))

if link_263 and link_452:
    volume_263 = find_volume(link_263)
    volume_452 = find_volume(link_452)
    diff = max(volume_263, volume_452) - min(volume_263, volume_452)
    print (diff)