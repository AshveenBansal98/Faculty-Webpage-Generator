from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys
html = urlopen("https://scholar.google.co.in/citations?user=Myp5iZkAAAAJ&hl=en")
#html = urlopen(sys.argv[1])
soup = BeautifulSoup(html, "lxml")

article = []
year = []
authors = []
citations = []
for table in soup.findAll('table', attrs = {'id': 'gsc_a_t'} ):
    for row in table.findAll('tr', attrs = {'class': 'gsc_a_tr'} ):
        for a in  row.findAll('a', attrs = {'class': 'gsc_a_at'} ):
            article.append(a.text)
        count = 0
        for div in  row.findAll('div', attrs = {'class': 'gs_gray'} ):
            count = count + 1
            if count == 1:
                authors.append(div.text)
        for tags in row.findAll('td', attrs = {'class': 'gsc_a_c'} ):
            for a in  tags.findAll('a', attrs = {'class': 'gsc_a_ac gs_ibl'} ):
                citations.append(a.text)
        for tags in row.findAll('td', attrs = {'class': 'gsc_a_y'} ):
            for a in  tags.findAll('span', attrs = {'class': 'gsc_a_h gsc_a_hc gs_ibl'} ):
                year.append(a.text)

print(article)
