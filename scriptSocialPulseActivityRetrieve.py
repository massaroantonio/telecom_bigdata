import urllib2
import json
import os.path
APP_ID="2d01b66d&"
APP_KEY="2cad535e1d4cec1de738c9ec50c0c563"
URL_BASE="https://api.dandelion.eu/datagems/v2/SpazioDati/social-pulse-2015-roma/data?"
LIMIT=0
OFFSET=0
monthRange=[3,4]
dayRange=[1,1] #one entry per month
hoursRange=range(24) #one entry per hour
#open output file, if existing delete
nameFileOut='twitterVolume.csv';
if os.path.isfile(nameFileOut):
		os.remove(nameFileOut);
fileOut=open(nameFileOut,'w+')
#now create calls to SpazioDati APIs
for i in range(len(monthRange)):
	for j in range(1,dayRange[i]+1):
		for t in hoursRange:
			DATE_TIME_STRING = "2015-"+format(monthRange[i],'02d')+"-"+format(j,'02d')+"T"+format(t,'02d');
			URL_FULL=URL_BASE+"$limit="+str(LIMIT)+'&$where=starts_with(created,+"'+DATE_TIME_STRING+'")&$offset='+str(OFFSET)+"&$app_id="+APP_ID+"&$app_key="+APP_KEY;
			response=urllib2.urlopen(URL_FULL)
			data=json.load(response)
			counter=data["count"]
			fileOut.write(DATE_TIME_STRING+","+str(counter)+"\n")
#now close the file
fileOut.close()
