import requests
from bs4 import BeautifulSoup
import re
import json
from tqdm import tqdm

baseUrl = 'https://www.component-hk.net'
url = 'https://www.component-hk.net/products/Capacitors/Aluminum-Polymer-Capacitors.html'

products = [baseUrl, url]
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('div', id='page')
totalPages = int(re.search(r"total page \d+", str(results[0])).group().split()[-1])

for i in tqdm(range(totalPages), desc='pages'):
    if i == 0:
        page = requests.get(url)
    else:
        newUrl = url.split('.')
        newUrl[-2] = newUrl[-2]+f"_{i+1}"
        newUrl = '.'.join(newUrl)
        page = requests.get(newUrl)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all('div', class_='items clearfix')
    for result in results:
        #print(i, result, end='\n\n')
        products.append({})
        products[-1]['url'] = re.search(r"\/product\/.+\.html", str(result)).group()
        products[-1]['image'] = re.search(r'src=".+"', str(result)).group().split('"')[1]
        products[-1]['part#'] = re.search(r'Part#:.+\/a', str(result)).group().split('>')[-1].split('<')[0]
        products[-1]['supplierUrl'] = re.search(r"\/supplier\/.+.html", str(result)).group()
        products[-1]['supplier'] = ' '.join(products[-1]['supplierUrl'].split('/')[-1].split('.')[0].split('-'))
        products[-1]['description'] = re.search(r"n:<\/b><s>[^<].+<\/s", str(result)).group().split('<')[-2].split('>')[1]
        products[-1]['stock'] = re.search(r'k:<\/b><s>\d+', str(result)).group().split('>')[-1]
        try:
            products[-1]['price'] = re.search(r"\$\d+\.*\d*", str(result)).group()
        except AttributeError:
            products[-1]['price'] = 'Unavailable'
        #print(products[-1], end='\n\n')
    #print()

with open(url.split('/')[-1].split('.')[0]+'.json', 'w') as f:
    json.dump(products, f, indent=4)