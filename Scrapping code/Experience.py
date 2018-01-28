from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys

html = urlopen("file://" + sys.argv[1])
soup = BeautifulSoup(html, "lxml")
# python3 Education.py /home/ashveen/Downloads/file.html > Experience.csv 
designations = []
companies = []
dates = []

for tags in soup.findAll('section', attrs = {'class': 'pv-profile-section experience-section ember-view'} ):
	for h3 in  tags.findAll('h3', attrs = {'class': 'Sans-17px-black-85%-semibold'} ):
		designations.append(h3.text)
	for span in  tags.findAll('span', attrs = {'class': 'pv-entity__secondary-title'} ):
		companies.append(span.text)
	for h4 in  tags.findAll('h4', attrs = {'class': 'pv-entity__date-range inline-block Sans-15px-black-70%'} ):
		count = 0
		for span in h4.findAll('span'):
			count = count + 1
			if count == 2:
				dates.append(span.text)



for i in range(0, len(designations)):
	print(designations[i] + "|" + companies[i] + "|" + dates[i])

	


