import requests
from bs4 import BeautifulSoup

page = requests.get("http://www.ugb.edu.sv") 
soup = BeautifulSoup(page.content, 'html.parser') 
#soup.find_all('li') 

for i in range(len(soup.find_all('li'))):
    print (soup.find_all('li')[i].get_text())