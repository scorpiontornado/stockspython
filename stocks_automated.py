from selenium import webdriver
from lxml import html

def share_profit(old_value, new_value, money_spent):
	shares_bought = money_spent / old_value
	
	return (shares_bought * new_value) - (shares_bought * old_value)

def share_percent(money_spent_total, profit):
	return profit / money_spent_total * 100

share_list = [
    {
        "name": "STW",
        "old_price": 58.34,
        # "new_price": 60.8,
        # "new_price": 62.79,
        # "new_price": 61.10, # 12/8/19
        "amount_bought": 5017.24,
        "douse_bought": 9976.14,
    },
    {
        "name": "APX",
        "old_price": 24.13,
        # "new_price": 27.39,
        # "new_price": 30.28,
        # "new_price": 25.43,
        "amount_bought": 1520.19,
    },
    {
        "name": "A2M",
        "old_price": 15.2,
        # "new_price": 14.84,
        # "new_price": 16.33,
        # "new_price": 15.23,
        "amount_bought": 1489.6,
    },
    {
        "name": "COL",
        "old_price": 12.6,
        # "new_price": 12.56,
        # "new_price": 13.98,
        # "new_price": 13.52,
        "amount_bought": 1008.8,
    },
    {
        "name": "QAN",
        "old_price": 5.3,
        # "new_price": 5.47,
        # "new_price": 5.79,
        # "new_price": 5.74 ,
        "amount_bought": 498.20,
    },
    {
        "name": "WES",
        "old_price": 36.02,
        # "new_price": 38.08,
        # "new_price": 39.30,
        # "new_price": 39.11,
        "amount_bought": 396.22,
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

douse = share_profit(share_list[0]["old_price"], share_list[0]["new_price"], share_list[0]["douse_bought"])

if(shares > douse):
	my_string = "Congrats, you made more money than if you had only\ninvested in STW!"
elif(shares == douse):
	my_string = "Somehow, you would have made the same amount of money\nif you had only invested in STW!. You are in the Matrix!"
else:
    my_string = "Drat!\nYou would have made more if you had only invested in STW!"

profitStr = "Your profit, from spending $" + str(money_spent) + ": $" + str(round(shares, 2)) + " (to 2dp)\n\nIf you had bought $" + str(share_list[0]["douse_bought"]) + " of ASX 200 Fund (ASX: STW),\nyour profit would be: $" + str(round(douse, 2)) + " (to 2dp)\n\n" + my_string

pctStr = "Your percentage profit: " + str(round(shares_percent, 4)) + "% (to 4dp)\n\nIf you had bought $" + str(share_list[0]["douse_bought"]) + " of ASX 200 Fund (ASX: STW),\nyour percentage profit would be: " + str(round((share_percent(share_list[0]["douse_bought"], douse)), 4)) + "% (to 4dp)"



print(profitStr, pctStr, sep='\n\n', end='\n\n')
print("Individual breakdown:", indProfit, indPctPr, sep='\n')
