from lxml import html
import requests
import json
import sys
import re

page = requests.get('http://ucsd.edu/catalog/front/courses.html')
#tree = html.fromstring(page.content)

f = open('url.data', 'r+')
pattern = r'courses/(.*?).html'
content = page.content

arrays = re.findall(pattern,content)
#print(content)
for array in arrays:
	f.write(array)
	f.write(".html\n")
f.close()
