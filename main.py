import requests
from bs4 import BeautifulSoup
import csv

def get_data(url,sp):
    r = requests.get(url, headers=HEADERS, timeout=130)
    html=r.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('main' ,class_='d_5')
    name=items.find("header", class_="tA").find('h1').get_text()
    print('name',name)
    
    items = soup.find('aside' ,class_='bT')
    cost=items.find("div", class_="C_").get_text().split('\xa0₽')
    print('cost',cost)

    data=[]
    for i in soup.find_all('div' ,class_='pn'):
            print(i.get_text())
            data.append(i.get_text())
    sp.writerow({'id': data[1], 'title': name,'price': cost[1],'promo_price': cost[0],'discount': cost[2],'code': data[3],'country': data[5],'sizes': data[7],'weight': data[9],'url': url})


HEADERS = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}
add=''
count=1
while True:
    try:
        url = 'https://www.detmir.ru/catalog/index/name/lego/'+add
        r = requests.get(url, headers=HEADERS, timeout=130)

        html=r.text
        soup = BeautifulSoup(html, 'html.parser')

        items = soup.find(id='app-container')

        csvfile = open('toys.csv', 'w', newline='', encoding='utf-8')
        fieldnames = ['id', 'title', 'price', 'promo_price', 'discount','code','country','sizes','weight', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for i in items.find_all("div", class_="yU"):
            print(i.find('a').get('href'))
            get_data(i.find('a').get('href'),writer)
        count+=1
        add='page/'+str(count)
    except:
        csvfile.close()
        break

print('Выполнено!')



    
