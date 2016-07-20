import lxml
from lxml import html
import requests
import json
import sys
import re


f = open('final_res', 'r+')

with open('url2') as urlfile:
	for line in urlfile:
		url = "http://ucsd.edu/catalog/courses/"+line
		#url = "http://ucsd.edu/catalog/courses/CSE.html"

		url = url.strip()
		f.write(url)
		f.write('\n')
		page = requests.get(url)
		tree = html.fromstring(page.content)
		#subject = tree.xpath( "//h1[@class=\"noTopMargin\"]/text()")
		#subject[0] = re.sub('[\t\n\r]', ' ', subject[0])
		#print subject[0]
		ids = tree.xpath( "//a[@id and @name]/@id" )
		#print ids

		cname = tree.xpath( "//p[@class=\"course-name\"]/text() | //p[@class=\"course-name\"]/descendant::*/text()" )
		cdep = tree.xpath( "//p[@class=\"course-descriptions\"]/text() | //p[@class=\"course-descriptions\"]/descendant::*/text()" )

		#print cname
		#print cdep[:30]
		final = []
		cdep2 = []

		#print cname
		for item in range(len(cname)):
			cname[item] = cname[item].strip(' \t\n\r ')
			cname[item] = re.sub('[\t\n\r]', '', cname[item])
			while "  " in cname[item]:
				cname[item] = re.sub('  ', ' ', cname[item])
			f.write (cname[item].encode("utf-8"))
			f.write('\n')
		f.write('\n')
f.close()
