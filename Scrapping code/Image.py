from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys
import re

html = urlopen("file://" + sys.argv[1])
soup = BeautifulSoup(html, "lxml")
#python3 Image.py /home/ashveen/Downloads/file.html > Education.csv 

url = ""
for div in soup.findAll('div', attrs = {'class': ' presence-entity__image EntityPhoto-circle-8 ember-view'} ):
	url = div.attrs

url2 = str(url) 
link = re.findall(r'"([^"]*)"', url2)
print(len(link))
print(link[0])

