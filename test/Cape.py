import json
import re
import lxml
from bs4 import BeautifulSoup
import sys
import requests

def makePretty(search):
	result = "".join(i for i in search.text if ord(i)<128)
	result.rstrip().strip()
	return result

url = "http://cape.ucsd.edu/responses/Results.aspx?Name=&CourseNumber=CSE+12"
user_agent = {'User-agent': 'Mozilla/5.0'}
result = requests.get(url, headers=user_agent)
soup = BeautifulSoup(result.content, 'lxml')
found = (soup.find_all("tr", class_=re.compile(r"(odd|even)")))
print len(found)
count = 0
for section in found:
	
	## INSTR NAME
	iName = section.find_next("td")
	instrName = makePretty(iName)

	## CHECK IF CORRECT CLAS
	cName = iName.find_next("td")
	className = makePretty(cName)
	if ("CSE 12"+" ") not in className:
		#print(className + " does not match " + "CSE 12")
		continue

	## TERM
	cTerm = cName.find_next("td")
	classTerm = makePretty(cTerm)

	# ENROLL
	cEnroll = cTerm.find_next("td")
	classEnroll = makePretty(cEnroll)

	#SUBMITTED
	cSubmitted = cEnroll.find_next("span")
	classSubmitted = makePretty(cSubmitted)

	## RECONMMEND CLASS
	rClass = cSubmitted.find_next("span")
	recommenClass = makePretty(rClass)

	## RECOMMEND INSTR
	rInstr = rClass.find_next("span")
	recommendInstr = makePretty(rInstr)

	## STUDY HRS
	sHours = rInstr.find_next("span")
	studyHours = makePretty(sHours)

	## AVERAGE GRADE EXPECTED
	avgExpected = sHousr.find_next("span")
	averageExpected = makePretty(avgExpected)

	## AVERAGE GRADE RECEIVED
	avgReceived = sHousr.find_next("span")
	averageReceived = makePretty(avgReceived)

	count = count + 1
	print (instrName)
	print (className)
	print (classTerm)
	print (classEnroll)
	print (classSubmitted)
	print (recommendClass)
	print (recommendInstr)
	print (studyHours)
	print (averageExpected)
	print (averageReceived)
	print ("\n")

print (count)
