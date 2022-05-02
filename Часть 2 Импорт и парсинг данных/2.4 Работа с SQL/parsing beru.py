from cgitb import html
from os import link
import sqlite3
import requests
from bs4 import BeautifulSoup
import time
headers = {"User-Agent": "ittensive-python-scraper/1.0 (+https://www.ittenasive.com)"}
#t = time.now()
r = requests.get("url", headers = headers)
#response_time = time.now() - t
#2-3 rps, Crawl-Delay, response.time*2-3
#time.sleep(round(response_time * 3))
#https://market.yandex.ru/brands--lg/153074?was_redir=1&rs=eJwzYgpgBAABcwCG&rt=5&suggest_text=lg&cpa=1
#/product--stiralnaia-mashina-scandilux-lm2t-6087-b/854165034?cpc=6wvoR6KBCa_CyeQCQWgaYOQFk1q0acEwULIn0RYljBd-XAs8-PP9CIZlUyf4rlQb9A3KC7Ec9X4e8osBSv_wJUgkiUzyketQbHhiTvFfOkmu9cZHGZiSazXcUpZ8NYWOWqqCafUrUzB0VXkNNlRwPAG_N6qwlr1Itt8r8atVlSnEUKqdoOPVgA%2C%2C&sku=854165034&do-waremd5=6tgJsOje5Ao83V89naFxNg&offerid=6tgJsOje5Ao83V89naFxNg&cpa=1
def find_data (link):
    r=requests.get('https://market.yandex.ru'+link)
    html=BeautifulSoup(r.content)
    print(html)

find_data('/product--stiralnaia-mashina-scandilux-lm2t-6087-b/854165034?cpc=6wvoR6KBCa_CyeQCQWgaYOQFk1q0acEwULIn0RYljBd-XAs8-PP9CIZlUyf4rlQb9A3KC7Ec9X4e8osBSv_wJUgkiUzyketQbHhiTvFfOkmu9cZHGZiSazXcUpZ8NYWOWqqCafUrUzB0VXkNNlRwPAG_N6qwlr1Itt8r8atVlSnEUKqdoOPVgA%2C%2C&sku=854165034&do-waremd5=6tgJsOje5Ao83V89naFxNg&offerid=6tgJsOje5Ao83V89naFxNg&cpa=1')

