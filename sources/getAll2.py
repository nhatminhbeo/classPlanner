import lxml
from lxml import html
import requests
import json
import sys
import re
from bs4 import BeautifulSoup


f = open('final_res2', 'r+')
list = []
with open('url2') as urlfile:
	for line in urlfile:

		url = "http://ucsd.edu/catalog/courses/"+line
		url = url.strip()
		#print(url)
		#print('\n')

		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'lxml')
		for cnamee in soup.find_all("p", class_='course-name'):

			dict = { "code":"", "unit":"", "title":"", "description":"" }

			#### SKIP EDGE CASE OF BLANK <p class="course-name> ####
			a = re.search(r"[a-zA-Z0-9]", cnamee.text.encode("utf-8"))
			if (a == None):
				continue

			#### GET COURSE CODE ####
			ccodee = cnamee.find_previous("a")
			ccode = ccodee.get("name")
			if (ccode != None):
				for char in range(len(ccode)):
					if ccode[char].isdigit():
						ccode = ccode[:char] + " " + ccode[char:]
						break
				if (ccode.upper() in cnamee.text.upper()) or len(ccode)<=9:
					dict["code"] = ccode.encode("utf-8")
					f.write(ccode.encode("utf-8"))
					f.write("\n")
				else:
					ccodee = re.search(r"[a-zA-Z]+ [0-9A-Z]+", cnamee.text.encode("utf-8"))
					if (ccodee != None):
						dict["code"] = ccodee.group()
						f.write(ccodee.group().encode("utf-8"))
						f.write("\n")


			else:
				ccodee = re.search(r"[a-zA-Z]+ [0-9A-Z]+", cnamee.text.encode("utf-8"))
				if (ccodee != None):
					dict["code"] = ccodee.group()
					f.write(ccodee.group().encode("utf-8"))
					f.write("\n")

			#### GET COURSE UNIT ####
			openindex = cnamee.text.rfind('(')
			if (openindex != -1):
				cunit = cnamee.text[openindex:]
				dict["unit"] = cunit
				f.write(cunit.encode("utf-8"))
				f.write("\n")

			#### GET COURSE TITLE ####
			cname = cnamee.text
                        cname = cname.strip(' \t\n\r ')
                        cname = re.sub('[\t\n\r]', '', cname)
                        while "  " in cname:
                                cname = re.sub('  ', ' ', cname)
			dict["title"] = cname
			f.write(cname.encode("utf-8"))
			f.write("\n")

			#### GET COURSE DESCRIPTION ####
			cdepe = cnamee.find_next("p")
			cdep = cdepe.text
			cdep = cdep.strip(' \t\n\r ')
                        while "  " in cdep:
                                cdep = re.sub('  ', ' ', cdep)
			while (re.search('[\t\n\r]', cdep) != None):
				cdep = re.sub('[\t\n\r]', '', cdep)
			dict["description"] = cdep
			f.write(cdep.encode("utf-8"))
			f.write("\n\n")

			list.append(dict)

	
for dict in list:
	dict["unit"] = ''.join(i for i in dict["unit"] if ord(i)<128)
	dict["title"] = ''.join(i for i in dict["title"] if ord(i)<128)
	dict["code"] = ''.join(i for i in dict["code"] if ord(i)<128)
	dict["description"] = ''.join(i for i in dict["description"] if ord(i)<128)
js = open ("final_res.json", "r+")
json.dump(list,js)
js.close()			
f.close()

