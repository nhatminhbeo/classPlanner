import lxml
from lxml import html
import requests
import json
import sys
import re


def edgeCase(cname, cdep, item):

	if "ANSC 100" in cname[item]:
		cdep.insert(item, "Course usually taught by visiting faculty in sociocultural anthropology. Course will vary in title and content. When offered, the current description and title is found in the current Schedule of Classes and the anthropology department website. (Can be taken a total of four times as topics vary.) Prerequisites: upper-division standing or consent of instructor. (Formerly known as ANGN 100.)")

	if "ANSC 164" in cname[item]:
		cdep.insert(item, "Basic concepts and theory of medical anthropology are introduced and applied to comparison of medical systems including indigenous and biomedical, taking into account cross-cultural variation in causal explanation, diagnosis, perception, management, and treatment of illness and disease. Prerequisites: upper-division standing.")

	if "ANTH 201" in cname[item]:
		cdep.insert(item, "Course usually taught by visiting faculty in anthropological archaeology. Course will vary in title and content. When offered, the current description and title is found in the current Schedule of Classes on TritonLink, and the Department of Anthropology website. (Can be taken a total of four times as topics vary.) (Formerly known as ANGR 201.)")


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
		#cdep = tree.xpath( "//p[@class=\"course-descriptions\"]/text()" )
		pattern = r'course-descriptions\">(.*?)<\/p'
		cdep = re.findall(pattern, page.content, re.I|re.S)
		#print(cdep)
		#print cname
		#print cdep[:30]
		final = []
		cdep2 = []

		#print cname
		item2 = -1
		for item in range(len(cname)):
			item2 = item2 + 1
			if ((page.content.decode("utf-8").find(cname[item])) < (page.content.find(cdep[item2]))):
				cdep.insert(item2, "")
			cname[item] = cname[item].strip(' \t\n\r ')
			cname[item] = re.sub('[\t\n\r]', '', cname[item])
			while "  " in cname[item]:
				cname[item] = re.sub('  ', ' ', cname[item])
			#edgeCase(cname, cdep, item)
			f.write (cname[item].encode("utf-8"))
			f.write('\n')
			f.write(cdep[item2])
			f.write('\n')
			f.write('\n')
			f.write('\n')
		f.write('\n')
f.close()

