import requests
from bs4 import BeautifulSoup

url = 'https://testnet.theparallel.io/market/shop/paragon'

req = requests.get(url)
#print(req.content)

soup = BeautifulSoup(req.content,'lxml')
print("Title")
print("Title : ",soup.title)

print("---------Content-------------")
content_ele = soup.select_one("#application")
print(content_ele)