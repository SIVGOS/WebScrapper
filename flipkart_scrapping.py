import requests
from bs4 import BeautifulSoup as bt
item = 'shoes'
url = "https://www.flipkart.com/search?q=" + item + "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
source=requests.get(url).text
'''
fid = open('test_html.txt','w')
print(source.encode('utf-8'),file = fid)
fid.close()
'''
soup=bt(source,'lxml')
match = soup.find_all('div',class_ = '_1vC4OE')
for z in match:
    print(z)
