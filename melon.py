import requests
from bs4 import BeautifulSoup
import pandas as pd

# 웹에 접속
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
r = requests.get("https://www.melon.com/chart/index.htm", headers=header)
print(r)

# html 정보 가지고오기
soup = BeautifulSoup(r.text, 'html.parser')

#1-100까지 리스트 만들기
rank = []
for i in range(1,101):
    rank.append(i)
print(rank)

# 노래 제목 리스트 만들기
tlist = []
title = soup.select('div.ellipsis.rank01 > span >a')
for t in title:
    tlist.append(t.text)

# 가수 리스트 만들기
alist = []
artist = soup.select('div.ellipsis.rank02 > span >a')
for a in artist:
    alist.append(a.text)

df3 = pd.DataFrame({'순위': rank,
                    '제목': tlist,
                    '가수': alist})

df3.to_csy('melon100.csv', index=False)