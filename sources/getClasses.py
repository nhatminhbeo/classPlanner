from lxml import html
import requests
import json
import sys

page = requests.get('http://ucsd.edu/catalog/courses/CSE.html')
tree = html.fromstring(page.content)

cname = tree.xpath( "//p[@class=\"course-name\"]/text()" )
cdep = tree.xpath( "//p[@class=\"course-descriptions\"]/text() | //p[@class=\"course-descriptions\"]/descendant::*/text()" )


classes = {}

for i in range(len(cname)):
	classes[cname[i]] = cdep[i:i+2]


f = open('result', 'r+')
json.dump(classes, f)
f.close()
