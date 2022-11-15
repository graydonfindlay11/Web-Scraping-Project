

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

url = 'https://www.investing.com/crypto/'

req = Request(url, headers=headers)

webpage = urlopen(req).read()




soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title
stock_rows = soup.findAll("tr")

print()
print(' ---------------------------------------------------------------')
print("|",title.text,"|")
print(' ---------------------------------------------------------------')
print('|               Top Five Current Cryptocurrencies:              |')
print(' ---------------------------------------------------------------')
print()


for row in stock_rows[1:6]:
    td = row.findAll("td")

    number = (td[0].text.strip())
    name = (td[2].text.strip())
    ticker = (td[3].text.strip())
    price = (td[4].text)
    mcap = (td[5].text.strip())
    daychange = (td[8].text.strip())
    

    priceholder = float(td[4].text.replace(",",""))
    changeholder = float(td[8].text.replace("+","").replace("%","")) / 100
    new_price = round((priceholder + (priceholder * changeholder)), 4)
    print(f"Ranking:     {number}")
    print(f"Name:        {name}")
    print(f"Ticker:      {ticker}")
    print(f"Price:       ${price}")
    print(f"Market Cap:  {mcap}")
    print(f"% Change:    {daychange}")
    print(f"New Price:   ${new_price:,.4f}")
    print()
    x = input()


#TWILIO 
import keys
from twilio.rest import Client
client = Client(keys.accountSID, keys.authToken)

TwilioNumber = "+16802198519"

myCellPhone = "+19037055343"




for row in stock_rows[1:2]:
    td = row.findAll("td")
    bitcoin = float(td[4].text.replace(",",""))
    if bitcoin < 40000:
        textmsg = client.messages.create(to=myCellPhone, from_=TwilioNumber, body = "\n Bitcoin has dropped below $40,000")
        print("-------------------------------------")
        print("Bitcoin Alert Message Status:", textmsg.status)


for row in stock_rows[2:3]:
    td = row.findAll("td")
    eth = float(td[4].text.replace(",",""))
    if eth < 3000:
        textmsg = client.messages.create(to=myCellPhone, from_=TwilioNumber, body = "\n Ethereum has dropped below $3,000")
        print("-------------------------------------")
        print("Ethereum Alert Message Status:", textmsg.status)
        print("-------------------------------------")
   









   




