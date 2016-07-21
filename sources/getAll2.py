import lxml
from lxml import html
import requests
import json
import sys
import re
from bs4 import BeautifulSoup


f = open('final_res2', 'r+')

with open('url2') as urlfile:
	for line in urlfile:
		url = "http://ucsd.edu/catalog/courses/"+line
		url = url.strip()
		#print(url)
		#print('\n')

		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'lxml')
		for cnamee in soup.find_all("p", class_='course-name'):
			cname = cnamee.text
                        cname = cname.strip(' \t\n\r ')
                        cname = re.sub('[\t\n\r]', '', cname)
                        while "  " in cname:
                                cname = re.sub('  ', ' ', cname)
			f.write(cname.encode("utf-8"))
			f.write("\n")

			cdepe = cnamee.find_next("p")
			cdep = cdepe.text
			cdep = cdep.strip(' \t\n\r ')
                        while "  " in cdep:
                                cdep = re.sub('  ', ' ', cdep)
			while (re.search('[\t\n\r]', cdep) != None):
				cdep = re.sub('[\t\n\r]', '', cdep)
			f.write(cdep.encode("utf-8"))
			f.write("\n\n")
			
f.close()

