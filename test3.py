from selenium import webdriver
from lxml import html

def share_profit(old_value, new_value, money_spent):
	shares_bought = money_spent / old_value
	
	return (shares_bought * new_value) - (shares_bought * old_value)

def share_percent(money_spent_total, profit):
	return profit / money_spent_total * 100

share_list = [
    {
        "name": "RIO",
        "old_price": 100.467,
        "amount_bought": 100.467,
    },
    {
        "name": "BHP",
        "old_price": 40.850,
        "amount_bought": 40.850,
    }
]

browser = webdriver.Chrome('/Users/nicholas/Desktop/stockspython/chromedriver') #replace with .Firefox(), or with the browser of your choice
for i in share_list:
    url = "https://www.asx.com.au/asx/share-price-research/company/" + i["name"]
    browser.get(url) #navigate to the page
    innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
    htmlElem = html.document_fromstring(innerHTML)
    i["new_price"] = float(htmlElem.xpath('//span[@class="ng-binding"]/text()')[1])

browser.quit()

money_spent = 0
shares = 0
indProfit = "Profit (to 2 d.p.):"
indPctPr = "Percentage Profit (to 4 d.p.):"

for i in share_list:
    # print(i)
    money_spent += i["amount_bought"]
    shares += share_profit(i["old_price"], i["new_price"], i["amount_bought"])
    temp = round(share_profit(i["old_price"], i["new_price"], i["amount_bought"]), 2)
    indProfit = indProfit + "\n" + i["name"] + ": " + str(temp)
    temp = round(share_percent(i["amount_bought"], (share_profit(i["old_price"], i["new_price"], i["amount_bought"]))), 4)
    indPctPr = indPctPr + "\n" + i["name"] + ": " + str(temp)

shares_percent = share_percent(money_spent, shares)

profitStr = "Your profit, from spending $" + str(money_spent) + ": $" + str(round(shares, 2)) + " (to 2dp)"

pctStr = "Your percentage profit: " + str(round(shares_percent, 4)) + "% (to 4dp)"



print(profitStr, pctStr, sep='\n\n', end='\n\n')
print("Individual breakdown:", indProfit, indPctPr, sep='\n')

