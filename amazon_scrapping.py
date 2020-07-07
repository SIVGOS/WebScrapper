import requests
from bs4 import BeautifulSoup as bt
item = 'shoes'
url = "https://www.amazon.in/s?k="+item+"&ref=nb_sb_noss_2"
source=requests.get(url).text
soup=bt(source,'lxml')
pret = soup.prettify()
if len(pret) < 6000:
    error
else:
    k = 0
    while k < len(pret)-1000:
        z = pret.find('a-price-whole',k )
        if z == -1:
            break
        else:
            print(pret[z:z+50])
            k = z+10
'''
flag = 0
while flag == 0:
    source=requests.get(url).text
    soup=bt(source,'lxml')
    pret = soup.prettify()
    if len(pret)>6e3:
        flag = 1
        k = 0
        while k < len(pret)-1000:
            z = pret.find('a-price-whole',k )
            if z == -1:
                break
            else:
                print(pret[z:z+50])
                k = z+10
'''
