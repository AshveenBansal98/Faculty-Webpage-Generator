from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys

html = urlopen("file://" + sys.argv[1])
soup = BeautifulSoup(html, "lxml")
#python3 Education.py /home/ashveen/Downloads/file.html > Education.csv 

colleges = []
degree = []
branch = []
times = []
for tags in soup.findAll('section', attrs = {'class': 'pv-profile-section education-section ember-view'} ):
	for h3 in  tags.findAll('h3', attrs = {'class': 'Sans-17px-black-85%-semibold'} ):
		colleges.append(h3.text)
	count = 0
	for span in  tags.findAll('span', attrs = {'class': 'pv-entity__comma-item'} ):
		count = count + 1
		if count%2 == 1:
			degree.append(span.text)
		else:
			branch.append(span.text)
	for p in  tags.findAll('p', attrs = {'class': 'pv-entity__dates Sans-15px-black-70%'} ):
		count1 = 0
		for span in p.findAll('span'):
			count1 = count1 + 1
			if count1 == 2:
				x=0
				for time in span.findAll('time'):
					x = x+1
					if (x == 1):
						t = time.text
					if (x == 2):
						times.append(t + " - " + time.text)
						break

for i in range(0, len(times)):
	print(colleges[i] + "|" + degree[i] + "|" + branch[i] + "|" + times[i])
