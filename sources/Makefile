DATA_FILES 		= url.data classes.data
URL_DATA 		= url.data
CLASSES_DATA 		= classes.data
JSON_FILES 		= classes.json cape.json
CLASSES_JSON 		= classes.json
CAPE_JSON 		= cape.json
GET_URL 		= getUrl.py
GET_CLASSES 		= getClasses.py
GET_CAPE 		= getCape.py

default:
	touch ${DATA_FILES}${JSON_FILES}
	python ${GET_URL}
	python ${GET_CLASSES}
	python ${GET_CAPE}

clean:
	rm -f ${DATA_FILES} $(JSON_FILES)

new:
	make clean
	make default

url:
	rm -f ${URL_DATA}
	touch ${URL_DATA}
	python ${GET_URL}

classes:
	rm -f ${CLASSES_DATA} ${CLASSES_JSON}
	touch ${CLASSES_DATA} ${CLASSES_JSON}
	python ${GET_CLASSES}

cape:
	rm -f ${CAPE_JSON}
	touch ${CAPE_JSON}
	python ${GET_CAPE}

	
