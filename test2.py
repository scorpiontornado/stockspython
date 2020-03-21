from selenium import webdriver
# from bs4 import BeautifulSoup
from lxml import html

browser = webdriver.Chrome('/Users/nicholas/Desktop/stockspython/chromedriver') #replace with .Firefox(), or with the browser of your choice
# url = "http://www.google.com/search?q=ASX+STW"
url = "https://www.asx.com.au/asx/share-price-research/company/STW"
browser.get(url) #navigate to the page
innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
browser.quit()

# soup = BeautifulSoup(innerHTML.text, 'html.parser')

# #price = soup.find(class_='IsqQVc NprOob igIJnTgqqEm4-zJFzKq8ukm8')
# price = soup.findAll('span')
# print(price)

htmlElem = html.document_fromstring(innerHTML)

# clNm = 'ir9B7SyHXt3U-zJFzKq8ukm8'
# price = html.find_class(clNm)
# price  = htmlElem.xpath('//span[@class="ir9B7SyHXt3U-zJFzKq8ukm8"]')
# pBox = htmlElem.xpath('//div[@class="gsrt"]')
# price = htmlElem.xpath('//span[@class="NprOob"]/text()')

price = htmlElem.xpath('//span[@class="ng-binding"]/text()')[1]
print(price)