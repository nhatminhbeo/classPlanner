import json
import re
import lxml
from bs4 import BeautifulSoup
import sys
import requests

## FUNCTION TO MAKE CONTENTS READABLE
def makePretty(search):
	result = "".join(i for i in search.text if ord(i)<128)
	result = result.rstrip().strip()
	return result

## READ IN JSON CLASS FILE
data = open("classes.json").read()
data = json.loads(data)

## TO HOLD RESULTING CAPE DATA
res = {}

## GENERAL URL TO GET CAPES
masterURL = "http://cape.ucsd.edu/responses/Results.aspx?Name=&CourseNumber="

## DEBUG MESSAGE TO WATCH WHILE WAITING FKING HOURS
i = 0

## ITERATE THROUGH EACH CLASS
for entry in data:

	#if (i>10):
	#	break
	## DEBUG MESSAGE TO WATCH WHILE WAITING FIKING HOURS
	i = i + 1
	debug = open("cape.process", "a")
	debug.write(str(i)+ " out of " + str(len(data)) + "\n")
	debug.close()

	## DATA HOLDER
	sections = []
	res[entry["code"].upper()] = sections

	## GET THE CAPE PAGE
	url = masterURL + entry["code"]
	url = re.sub(' ', '+', url)
	user_agent = {'User-agent': 'Mozilla/5.0'}
	result = requests.get(url, headers=user_agent)
	result = result.content
	soup = BeautifulSoup(result, 'lxml')

	## START FINDING, BASED ON THE <tr class="odd|even"> tags
	found = (soup.find_all("tr", class_=re.compile(r"(odd|even)")))
	for section in found:
		
		## INSTR NAME
		iName = section.find_next("td")
		instrName = makePretty(iName)

		## CHECK IF CORRECT CLAS
		cName = iName.find_next("td")
		className = makePretty(cName)
		if (not className.startswith(entry["code"].upper()+" ")):
			#print(className + " does not match " + "CSE 12")
			continue

		## TERM
		cTerm = cName.find_next("td")
		classTerm = makePretty(cTerm)

		# ENROLL
		cEnroll = cTerm.find_next("td")
		classEnroll = makePretty(cEnroll)

		#SUBMITTED
		eSubmitted = cEnroll.find_next("span")
		evalSubmitted = makePretty(eSubmitted)

		## RECONMMEND CLASS
		rClass = eSubmitted.find_next("span")
		recommendClass = makePretty(rClass)

		## RECOMMEND INSTR
		rInstr = rClass.find_next("span")
		recommendInstr = makePretty(rInstr)

		## STUDY HRS
		sHours = rInstr.find_next("span")
		studyHours = makePretty(sHours)

		## AVERAGE GRADE EXPECTED
		avgExpected = sHours.find_next("span")
		averageExpected = makePretty(avgExpected)

		## AVERAGE GRADE RECEIVED
		avgReceived = avgExpected.find_next("span")
		averageReceived = makePretty(avgReceived)

		## ADD RESULT TO THE LIST
		current = {}
		current["InstrName"] = instrName
		current["className"] = className
		current["classTerm"] = classTerm
		current["classEnroll"] = classEnroll
		current["evalSubmitted"] = evalSubmitted
		current["recommendClass"] = recommendClass
		current["recommendInstr"] = recommendInstr
		current["studyHours"] = studyHours
		current["averageExpected"] = averageExpected
		current["averageReceived"] = averageReceived
		sections.append(current)
#print(res)
f = open("cape.json", "r+")
json.dump(res, f)
f.close()
