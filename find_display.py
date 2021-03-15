import json, os, re

url = 'https://www.component-hk.net/products/Capacitors/Aluminum-Polymer-Capacitors.html'
searchTerms = ['10-45V', '100UF']

htmlPage = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        .product {
            display: flex;
            flex-direction: row;
            width: 800px;
            margin: 0 auto;
            border-radius: 7px;
        }
        
        @media (max-width: 800px) {
            .product {
                width: 100%
            }
        }
        
        .product:hover {
            background-color: #ededed;
        }
        
        .item {
            display: flex;
            flex-direction: column;
        }
        
        .details {
            display: flex;
            flex-direction: row;
        }
        
        .img {
            margin-left: 3px;
            margin-right: 5px;
            margin-top: 3px;
            height: 80px;
            width: 80px;
            border-radius: 7px;
        }
        
        .part {
            overflow-wrap: anywhere;
            margin-right: 5px;
        }
        
        .supplier {
            overflow-wrap: anywhere;
        }
        
        .common {
            font-size: 13px;
            width: 160px;
        }
        
        .description {
            position: relative;
            top: 15%;
        }
    </style>
</head>
<body>'''
file = ''

# open data file and save data to variable
for i in os.listdir(os.getcwd()):
    if i.split('.')[0] in url.split('/')[-1].split('.'):
        file = i
if file == '':
    print('Data file not found, make sure you provided the correct link and you ran get_data.py on the same link.')
with open(file, 'r') as f:
    products = json.load(f)

# find all products matching the search terms
matchingProducts = []

for i in range(2, len(products)):
    fullMatch = True
    for term in searchTerms:
        if re.search(r'\d+\.*\d+-\d+\.*\d*[A-Z]+', term):
            iRange = [int(y) for y in re.findall(r'\d+', term)]
            letter = re.findall(r'[A-Z]+', term)[0]
            found = False

            for item in products[i]['description'].split():
                if re.search(fr'\d+\.*\d*{letter}+', item):
                    number = float(re.findall(r'\d+\.*\d*', item)[0])
                    if iRange[0] <= number <= iRange[1]:
                        found = True

            if not found:
                fullMatch = False
        elif term not in products[i]['description'].split():
            fullMatch = False
    if fullMatch:
        matchingProducts.append(products[i])

# sort by price (bubble sort)
for product in matchingProducts:
    if product['price'] == 'Unavailable':
        product['price'] = '$10000'

productsSorted = False
while not productsSorted:
    productsSorted = True
    for i in range(len(matchingProducts)-1):
        if float(matchingProducts[i]['price'].split('$')[1]) > float(matchingProducts[i+1]['price'].split('$')[1]):
            productsSorted = False
            hold = matchingProducts[i]
            matchingProducts[i] = matchingProducts[i+1]
            matchingProducts[i+1] = hold

for product in matchingProducts:
    if product['price'] == '$10000':
        product['price'] = '---'

# create html string
for product in matchingProducts:
    htmlPage += f'''
    <div class="product">
        <a href="{products[0]}{product['url']}"><img class="img" src="{products[0]}{product['image']}" width="75%" ></a>
        <div class="item">
            <div class="details">
                <div class="part common"><a href="{products[0]}{product['url']}">{product['part#']}</a></div>
                <div class="supplier common"><a href="{products[0]}{product['supplierUrl']}">{product['supplier']}</a></div>
                <div class="stock common">{product['stock']}</div>
                <div class="price common">{product['price']}</div>
            </div>
            <div class="description">{product['description']}</div>
        </div>
    </div><br>'''
htmlPage += '</body></html>'

with open(f"{url.split('/')[-1].split('.')[0]}|{'|'.join(searchTerms)}.html", 'w') as f:
    f.write(htmlPage)
