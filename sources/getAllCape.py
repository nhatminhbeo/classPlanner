import json
import re
import lxml
from bs4 import BeautifulSoup
import sys
import requests

## READ IN JSON CLASS FILE
data = open("final_res.json").read()
data = json.loads(data)
res = {}
## GENERAL URL TO GET CAPES
masterURL = "http://cape.ucsd.edu/responses/Results.aspx?Name=&CourseNumber="
i = 0
## ITERATE THROUGH EACH CLASS
for entry in data:

	## DEBUG
	i = i + 1
	print(str(i)+ " out of " + str(len(data)))


	sections = []
	res[entry["code"].upper()] = sections

	## GET THE CAPE PAGE
	url = masterURL + entry["code"]
	url = re.sub(' ', '+', url)
	result = requests.get(url)
	result = result.content
	soup = BeautifulSoup(result, 'lxml')


	## GET THE ODD SECTIONS
	for section in soup.find_all("td", class_="odd"):

		try:
		
			## INSTR NAME
			instrName = "".join(i for i in section.find_next("td").text if ord(i)<128)

			## CHECK IF CORRECT CLASS
			className = "".join(i for i in section.find_next("a", id="ctl00_ContentPlaceHolder1_gvCAPEs_ctl02_hlViewReport").text if ord(i)<128)
			if (entry["code"].upper()+" ") not in className:
				print(className + " does not match " + entry["code"].upper())
				continue

			## TERM
			term = "".join(i for i in section.find_next("td").find_next("td").find_next("td").text if ord(i)<128)

			## ENROLL
			enroll = "".join(i for i in section.find_next("a", align="right").text if ord(i)<128)

			## SUBMITTED
			submitted = "".join(i for i in section.find_next("span", id="ctl00_ContentPlaceHolder1_gvCAPEs_ctl02_lblCAPEsSubmitted").text if ord(i)<128)

			## RECOMMEND CLASS
			recommendClass = "".join(i for i in section.find_next("span", id="ctl00_ContentPlaceHolder1_gvCAPEs_ctl02_lblPercentRecommendCourse").text if ord(i)<128)
			
			## RECOMMEND INSTR
			recommendInstr = "".join(i for i in section.find_next("span", id="ctl00_ContentPlaceHolder1_gvCAPEs_ctl02_lblPercentRecommendInstructor").text if ord(i)<128)
			
			## STUDY HOUR
			studyHour = "".join(i for i in section.find_next("span", id="ctl00_ContentPlaceHolder1_gvCAPEs_ctl02_lblStudyHourse").text if ord(i)<128)

			## GRADE EXPECTED
			gradeExpected = "".join(i for i in section.find_next("span", id="ctl00_ContentPlaceHolder1_gvCAPEs_ctl02_lblGradeExpected").text if ord(i)<128)

			## GRADE RECEIVED
			gradeReceived = "".join(i for i in section.find_next("span", id="ctl00_ContentPlaceHolder1_gvCAPEs_ctl02_lblGradeReceived").text if ord(i)<128)

			## APPEND to the sections
			sections.append({"instrName":instrName, "term":term, "enroll":enroll, "submitted":submitted, "recommendClass":recommendClass, "recommendInstr":recommendInstr, "studyHour":studyHour, "gradeExpected":gradeExpeted, "gradeReceived":gradeReceived})

		except:

			print("An ERROR occured")
			sys.print_exc()

	## GET THE EVEN SECTIONS
	for section in soup.find_all("td", class_="even"):

		try:
		
			## INSTR NAME
			instrName = "".join(i for i in section.find_next("td").text if ord(i)<128)

			## CHECK IF CORRECT CLASS
			className = "".join(i for i in section.find_next("a", id="ctl00_ContentPlaceHolder1_gvCAPEs_ctl02_hlViewReport").text if ord(i)<128)
			if (entry["code"].upper()+" ") not in className:
				print(className + " does not match " + entry["code"].upper())
				continue

			## TERM
			term = "".join(i for i in section.find_next("td").find_next("td").find_next("td").text if ord(i)<128)

			## ENROLL
			enroll = "".join(i for i in section.find_next("a", align="right").text if ord(i)<128)

			## SUBMITTED
			submitted = "".join(i for i in section.find_next("span", id="ctl00_ContentPlaceHolder1_gvCAPEs_ctl02_lblCAPEsSubmitted").text if ord(i)<128)

			## RECOMMEND CLASS
			recommendClass = "".join(i for i in section.find_next("span", id="ctl00_ContentPlaceHolder1_gvCAPEs_ctl02_lblPercentRecommendCourse").text if ord(i)<128)
			
			## RECOMMEND INSTR
			recommendInstr = "".join(i for i in section.find_next("span", id="ctl00_ContentPlaceHolder1_gvCAPEs_ctl02_lblPercentRecommendInstructor").text if ord(i)<128)
			
			## STUDY HOUR
			studyHour = "".join(i for i in section.find_next("span", id="ctl00_ContentPlaceHolder1_gvCAPEs_ctl02_lblStudyHourse").text if ord(i)<128)

			## GRADE EXPECTED
			gradeExpected = "".join(i for i in section.find_next("span", id="ctl00_ContentPlaceHolder1_gvCAPEs_ctl02_lblGradeExpected").text if ord(i)<128)

			## GRADE RECEIVED
			gradeReceived = "".join(i for i in section.find_next("span", id="ctl00_ContentPlaceHolder1_gvCAPEs_ctl02_lblGradeReceived").text if ord(i)<128)

			## APPEND to the sections
			sections.append({"instrName":instrName, "term":term, "enroll":enroll, "submitted":submitted, "recommendClass":recommendClass, "recommendInstr":recommendInstr, "studyHour":studyHour, "gradeExpected":gradeExpeted, "gradeReceived":gradeReceived})

		except:

			print("An ERROR occured")
			sys.print_exc()
f = open("cape_res2.json", "r+")
json.dumps(res, f)
close(f)
