
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font




#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title
table_rows = soup.findAll("tr")
#table_columns = soup.findAll("tr")


print()
print(title.text)
print()
##
##
##
##my solution
for row in table_rows[1:6]:
    td = row.findAll("td")
    rank = (td[0].text)
    name = (td[1].text)
    totalgross = int(td[5].text.replace("$","").replace(",",""))
    distributor = (td[9].text)
    theatre = int(td[6].text.replace(",",""))
    avggross = round((totalgross / theatre) * 100,2)
    #print()
    print("Rank: ", rank)
    print("Name: ", name)
    print("Total Gross: ", totalgross)
    print("Distributor: ", distributor)
    print("Average Gross: ", avggross)
    #print(theatre)


    

#prof b solution

movie_rows = soup.findAll('tr')

for x in range(1,6):
    td = movie_rows[x].findAll('td')
    rank = td[0].text
    movie_name = td[1].text
    theater = td[6].text.replace(",","")
    gross = td[7].text.replace(",","")
    dis = td[9].text

    avg = (gross / theater)

    print(f"Rank : {rank}")
    print(f"Movie Name : {movie_name}")
    print(f"Total Gross : {gross:,.2f}")
    print(f"Distributor : {dis}")
    print(f"Average per Theater : {avg:,.2f}")



