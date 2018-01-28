from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys

html = urlopen("file://" + sys.argv[1])
soup = BeautifulSoup(html, "lxml")
#python3 Awards.py /home/ashveen/Downloads/file.html > Awards.csv

title = []
date = []
issuer = []
desc = []


for div in soup.findAll('div', attrs = {'class': 'pv-accomplishments-block__list-container'} ):
	for h4 in div.findAll('h4', attrs = {'class': 'pv-accomplishment-entity__title'} ):
		t = h4.text
		t = t.replace('honor title', '')
		t = t.replace('\n  ', '')
		t = t.replace('\n', '')
		title.append(t)

for p in soup.findAll('p', attrs = {'class': 'pv-accomplishment-entity__subtitle'} ):
	for span in p.findAll('span', attrs = {'class': 'pv-accomplishment-entity__date'} ):
		t = span.text
		t = t.replace('\nhonor date\n', '')
		t = t.replace('\n', '')
		t = t.replace('  ', '')
		date.append(t)
	for span in p.findAll('span', attrs = {'class': 'pv-accomplishment-entity__issuer'} ):
		t = span.text
		t = t.replace('\nhonor issuer\n', '')
		t = t.replace('\n', '')
		t = t.replace('  ', '')
		issuer.append(t)


for p in soup.findAll('p', attrs = {'class': 'pv-accomplishment-entity__description Sans-15px-black-70%'} ):
	t = p.text
	t = t.replace('\nhonor description\n', '')
	t = t.replace('\n', '')
	t = t.replace('  ', '')
	desc.append(t)

for i in range(0, len(title)):
	print(title[i] + "|" + date[i] + "|" + issuer[i] + "|")
	if i < len(desc):
		print(desc[i] + "\n")



return render(request, 'dashboard.html', context)


 

