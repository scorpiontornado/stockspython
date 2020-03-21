import requests
from bs4 import BeautifulSoup

url = 'http://www.google.com/search?q=ASX+STW'
url = 'https://www.asx.com.au/asx/share-price-research/company/STW'

page = requests.get(url)
# create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

#price = soup.find(class_='IsqQVc NprOob igIJnTgqqEm4-zJFzKq8ukm8')
price = soup.findAll('span')
print(price)