# ejemplo 2
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

url = urlopen("https://www.ugb.edu.sv/")
soup = BeautifulSoup(url.read(), "html.parser")
url.close()
#obtener link
f = csv.writer(open('enlace.csv','w'))
f.writerow(['Enlaces'])

for link in soup.find_all("a"):
    print(link.get("href"))
    f.writerow([link.get("href")])

#obtener texto
#title = soup.find("div", class_ = "body-innerwrapper")
#print(title)


page = requests.get("http://www.ugb.edu.sv")
soup = BeautifulSoup(page.content, 'html.parser')
#soup.find_all('li')

for i in range(len(soup.find_all('li'))):
    print(soup.find_all('li')[i].get_text())
