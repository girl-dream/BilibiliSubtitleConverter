# coding=utf-8
import gzip ,time
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

req = Request('https://www.tiobe.com/tiobe-index')
response = urlopen(req)
res_data = response.read()

if response.getheader("Content-Encoding") == "gzip":
    res_data = gzip.decompress(res_data)
response.close()

html_content = res_data.decode("utf-8")

# 获取当前日期的年、月、日
now = time.localtime()
year = now.tm_year
month = now.tm_mon
day = now.tm_mday

print(f"当前时间:{year}年{month}月{day}日")

soup = BeautifulSoup(html_content, "html.parser")
tbody = soup.find("tbody")
for tr in tbody.find_all("tr"):
    for i,td in enumerate(tr.find_all("td")):
        if i == 0:
            print(td.get_text(),end=' ')
        elif i == 4:
            print(td.get_text(),end='\n\n')
