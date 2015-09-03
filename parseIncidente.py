import json;
import os.path
#load input file with raw data from SpazioDati APIs
nameFile='twitterIncidente';
nameFileIn=nameFile+'.json';
json_data=open(nameFileIn).read();
data=json.loads(json_data);
#open output file
nameFileOut=nameFile+'.csv';
if os.path.isfile(nameFileOut):
		os.remove(nameFileOut);
fileOut=open(nameFileOut,'w+')
for i in range(len(data["items"])):
	timestamp=data["items"][i]["timestamp"]
	created=data["items"][i]["created"]
	fileOut.write(created+'\n')
fileOut.close()




