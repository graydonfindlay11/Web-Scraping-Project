import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request







random_chapter = random.randint(1,21)     #includes both limits, picks a chapter of John

if random_chapter < 10:
    random_chapter = '0' + str(random_chapter)
else:
    random_chapter = str(random_chapter)

url = 'https://ebible.org/asv/JHN' + random_chapter + '.htm'

print(url)






#PRELIM COPIED FROM OTHER webscraping
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)
                                     ##press command then click the link to open it

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title
print()
print(title.text)
print()

#bhoj way
page_verses = soup.findAll('div', class_='main')

#print(page_verses)

for verse in page_verses:
    verse_list = verse.text.split('.')

#print(verse_list)


myverse = random.choice(verse_list[:len(verse_list)-5])     #

print()
print(myverse)
print()

#Johns way
'''
paragraph = soup.findAll("div", attrs={"class":"p"})

print()
print(paragraph[1].text)
print()
'''


message = "Chapter" + random_chapter + "Verse" + myverse
print(message)

import keys
from twilio.rest import Client
client = Client(keys.accountSID, keys.authToken)

TwilioNumber = "+"

myCellPhone = "+"